"""Estimate the Base MNL and compare alternative model specifications.

This script:
1. Loads the mean-imputed dataset through the shared data loader.
2. Defines the four-mode walk, cycle, public-transport, and car utilities.
3. Estimates the Base MNL and its requested restricted/nested alternatives.
4. Calculates likelihood-ratio tests and goodness-of-fit statistics.
5. Exports fitted parameters, betas, and a model-comparison table.
6. Prints observed mode shares and runs requested sanity assertions.
"""

# Read/write the JSON beta file.
import json
# Import the numeric-prefixed shared module by name at runtime.
from importlib import import_module
# Use absolute paths so the script works from any working directory.
from pathlib import Path
from typing import Any, cast

# NumPy supplies numerical values and covariance calculations.
import numpy as np
# Pandas is used for DataFrame operations and CSV exports.
import pandas as pd
# SciPy provides the chi-square survival function for LR p-values.
from scipy.stats import chi2

# Biogeme supplies the choice-model expressions and estimation tools.
from biogeme import models
from biogeme.biogeme import BIOGEME
from biogeme.database import Database
from biogeme.expressions import Beta, Expression, ExpressionOrNumeric, Variable
from biogeme.nests import NestsForNestedLogit, OneNestForNestedLogit
from biogeme.results_processing.estimation_results import EstimationResults

# Numeric file prefixes cannot be imported with ordinary Python syntax,
# so the shared loader is retrieved through importlib.
load_clean_data = import_module("01_prepare_data").load_clean_data


# Repository and output locations are resolved relative to this script.
ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "outputs"
# CHOSEN_MODE contains the integer code for the observed chosen alternative.
CHOICE_COLUMN = "CHOSEN_MODE"
# Map human-readable alternative names to their integer choice codes.
ALTERNATIVES = {"Walk": 1, "Cycle": 2, "PT": 3, "Car": 4}


def beta(name: str) -> Beta:
    """Create an unconstrained, zero-starting-value Biogeme parameter.

    The four arguments passed to Beta are name, starting value, lower bound,
    upper bound, and fixed status. None means that a bound is not imposed.
    """
    return Beta(name, 0, None, None, 0)


def build_utilities(
    *,
    generic_travel_time: bool = False,
    summed_car_cost: bool = False,
) -> dict[int, ExpressionOrNumeric]:
    """Build the utility functions for the Base or a restricted MNL model.

    Set generic_travel_time=True to share one travel-time coefficient across
    all modes. Set summed_car_cost=True to share one coefficient across the
    three separate car-cost attributes. Both flags default to False for the
    full Base MNL specification.
    """
    # Variables represent dataset columns inside Biogeme expressions.
    tt_walk = Variable("TT_WALK")
    tt_cycle = Variable("TT_CYCLE")
    tt_pt = Variable("TT_PT")
    tt_car = Variable("TT_CAR")

    if generic_travel_time:
        # Restricted model: every mode uses the same travel-time coefficient.
        generic_tt = beta("B_TT_GENERIC")
        walk_time = cycle_time = pt_time = car_time = generic_tt
    else:
        # Base model: each mode has its own travel-time coefficient.
        walk_time = beta("B_TT_WALK")
        cycle_time = beta("B_TT_CYCLE")
        pt_time = beta("B_TT_PT")
        car_time = beta("B_TT_CAR")

    if summed_car_cost:
        # Restricted model: fuel, parking, and congestion use one cost effect.
        car_cost = beta("B_CAR_COST")
        fuel_cost = parking_cost = congestion_cost = car_cost
    else:
        # Base model: each car-cost attribute has a separate coefficient.
        fuel_cost = beta("B_FC_CAR")
        parking_cost = beta("B_PC_CAR")
        congestion_cost = beta("B_CC_CAR")

    # Utility values are keyed by the integer codes in CHOSEN_MODE.
    # Walk is the reference alternative and therefore has no ASC.
    utilities: dict[int, ExpressionOrNumeric] = {
        ALTERNATIVES["Walk"]: (
            walk_time * tt_walk
            + beta("B_WALK_IDX") * Variable("WALKABILITY_INDEX")
        ),
        ALTERNATIVES["Cycle"]: (
            # Cycle-specific constant, travel time, and built-environment terms.
            beta("ASC_CYCLE")
            + cycle_time * tt_cycle
            + beta("B_BIKE_IDX") * Variable("BIKEABILITY_INDEX")
            # Socio-demographic effects are allowed to differ by alternative.
            + beta("B_INC_CYCLE") * Variable("INCOME")
            + beta("B_AGE_CYCLE") * Variable("AGE")
            + beta("B_FEM_CYCLE") * Variable("FEMALE")
        ),
        ALTERNATIVES["PT"]: (
            # PT-specific constant and in-vehicle, waiting, access, and fare terms.
            beta("ASC_PT")
            + pt_time * tt_pt
            + beta("B_WT_PT") * Variable("WT_PT")
            + beta("B_AT_PT") * Variable("AT_PT")
            + beta("B_FARE_PT") * Variable("FARE_PT")
            + beta("B_AC_PT") * Variable("AC_PT")
            # Socio-demographic effects are again alternative-specific.
            + beta("B_INC_PT") * Variable("INCOME")
            + beta("B_AGE_PT") * Variable("AGE")
            + beta("B_FEM_PT") * Variable("FEMALE")
        ),
        ALTERNATIVES["Car"]: (
            # Car-specific constant, travel time, and three cost components.
            beta("ASC_CAR")
            + car_time * tt_car
            + fuel_cost * Variable("FC_CAR")
            + parking_cost * Variable("PC_CAR")
            + congestion_cost * Variable("CC_CAR")
            # Socio-demographic and household car-ownership effects.
            + beta("B_INC_CAR") * Variable("INCOME")
            + beta("B_AGE_CAR") * Variable("AGE")
            + beta("B_FEM_CAR") * Variable("FEMALE")
            + beta("B_CAROWN_CAR") * Variable("CAR_OWNERSHIP")
        ),
    }
    # Return utilities indexed exactly as the choice and availability mappings.
    return utilities


def availability() -> dict[int, ExpressionOrNumeric]:
    """Return the availability indicator for every mode."""
    return {
        ALTERNATIVES["Walk"]: Variable("AV_WALK"),
        ALTERNATIVES["Cycle"]: Variable("AV_CYCLE"),
        ALTERNATIVES["PT"]: Variable("AV_PT"),
        ALTERNATIVES["Car"]: Variable("AV_CAR"),
    }


def estimate_model(
    database: Database,
    name: str,
    log_probability: Expression,
) -> EstimationResults:
    """Create a Biogeme estimator and return converged estimation results."""
    # BIOGEME combines the database and probability formula for estimation.
    biogeme_type = cast(Any, BIOGEME)
    estimator = biogeme_type(database=database, formulas=log_probability)
    # The model name controls the generated Biogeme output filenames.
    setattr(estimator, "model_name", name)
    return estimator.estimate()


def log_likelihood(results) -> float:
    """Read the final log likelihood from a Biogeme EstimationResults object."""
    return float(results.final_loglikelihood)


def likelihood_ratio(
    unrestricted_ll: float,
    restricted_ll: float,
    degrees_of_freedom: int,
) -> tuple[float, float]:
    """Return a likelihood-ratio statistic and chi-square p-value.

    unrestricted_ll is the log likelihood for the larger model, while
    restricted_ll is the log likelihood for the nested smaller model.
    """
    # The LR statistic equals twice the difference in final log likelihood.
    statistic = 2 * (unrestricted_ll - restricted_ll)
    # The survival function gives P(chi-square >= observed statistic).
    return statistic, float(chi2.sf(statistic, degrees_of_freedom))


def share_table(df: pd.DataFrame, group: str | None = None) -> pd.DataFrame:
    """Build an overall or within-group observed mode-share table."""
    # Invert the alternative mapping to turn integer choices into names.
    mode_names = {code: name for name, code in ALTERNATIVES.items()}
    if group is None:
        # Normalize choice counts across the full 10,000-row dataset.
        shares = df[CHOICE_COLUMN].value_counts(normalize=True).sort_index()
        return pd.DataFrame(
            {"Mode": [mode_names[index] for index in shares.index], "Share": shares.values}
        )

    # Aggregate row counts by subgroup and chosen mode.
    grouped = (
        df.groupby([group, CHOICE_COLUMN], observed=True)
        .size()
        .rename("Count")
        .reset_index()
    )
    # Divide each subgroup-mode count by that subgroup's total count.
    grouped["Share"] = (
        grouped["Count"]
        / grouped.groupby(group, observed=True)["Count"].transform("sum")
    )
    # Replace mode codes with readable names for report-friendly output.
    grouped["Mode"] = grouped[CHOICE_COLUMN].map(mode_names)
    return grouped[[group, "Mode", "Share"]]


def export_parameter_table(results, beta_values: dict[str, float]) -> None:
    """Export model coefficients and PT values of time to a formatted CSV."""
    # Standard errors and t-statistics use Biogeme's Rao-Cramer covariance.
    covariance = results.rao_cramer_variance_covariance_matrix
    standard_errors = []
    t_statistics = []
    for parameter, estimate in beta_values.items():
        # Locate the parameter in the covariance matrix by name.
        index = results.get_parameter_index(parameter)
        variance = float(covariance[index, index])
        # A negative diagonal variance is invalid and should stop the run.
        if variance < 0:
            raise ValueError(f"Negative variance estimate for {parameter}: {variance}")
        # A standard error is the square root of the coefficient variance.
        standard_error = float(np.sqrt(variance))
        standard_errors.append(standard_error)
        # A t-statistic tests the null hypothesis that the coefficient is zero.
        t_statistics.append(estimate / standard_error)

    # Build the regular model-coefficient portion of the parameter table.
    table = pd.DataFrame(
        {
            "Parameter": list(beta_values),
            "Estimate": list(beta_values.values()),
            "Std. error": standard_errors,
            "t-statistic": t_statistics,
            "Type": "Model parameter",
        }
    )

    # Append each PT value of time as an additional reportable measure.
    vot_rows = []
    for label, time_parameter in (
        ("VOT_TT_PT", "B_TT_PT"),
        ("VOT_WT_PT", "B_WT_PT"),
        ("VOT_AT_PT", "B_AT_PT"),
    ):
        # A VOT is a time coefficient divided by the fare coefficient,
        # converted from £/minute to £/hour by multiplying by 60.
        vot_rows.append(
            {
                "Parameter": label,
                "Estimate": beta_values[time_parameter] / beta_values["B_FARE_PT"] * 60,
                "Std. error": np.nan,
                "t-statistic": np.nan,
                "Type": "Value of time (£/hour)",
            }
        )
    # Combine coefficients and VOT rows, then write four-decimal CSV output.
    table = pd.concat([table, pd.DataFrame(vot_rows)], ignore_index=True)
    table.to_csv(OUTPUT_DIR / "base_model_params.csv", index=False, float_format="%.4f")


def main():
    """Run all estimations, comparisons, exports, and printouts."""
    # load_clean_data performs cleaning, mean imputation, and group creation.
    df = load_clean_data()
    # Choice and availability fields must be complete before estimation.
    required = [
        "CHOSEN_MODE",
        "AV_WALK",
        "AV_CYCLE",
        "AV_PT",
        "AV_CAR",
    ]
    if df[required].isna().any().any():
        raise ValueError("Choice and availability fields must not contain missing values.")
    # Reject unexpected choice codes so an incorrect mapping is obvious.
    if not df[CHOICE_COLUMN].isin(ALTERNATIVES.values()).all():
        raise ValueError("CHOSEN_MODE must use the documented alternative codes 1 through 4.")

    # Create the output directory if it does not yet exist.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # The Biogeme database contains numerical data only; helper labels are excluded.
    database = Database(
        "Dataset_1_2026",
        df.drop(columns=["AGE_GROUP", "INCOME_GROUP"]),
    )
    # Biogeme expressions for observed choice and alternative availability.
    choice = Variable(CHOICE_COLUMN)
    avail = availability()

    # Estimate the full Base MNL with alternative-specific utility coefficients.
    base_utilities = build_utilities()
    base_results = estimate_model(
        database,
        "base_mnl",
        models.loglogit(base_utilities, avail, choice),
    )
    # Retain the final LL for goodness-of-fit and LR comparisons.
    base_ll = log_likelihood(base_results)

    # Estimate the generic travel-time restricted MNL.
    generic_results = estimate_model(
        database,
        "generic_travel_time_mnl",
        models.loglogit(
            build_utilities(generic_travel_time=True),
            avail,
            choice,
        ),
    )
    generic_ll = log_likelihood(generic_results)

    # Estimate the summed car-cost restricted MNL.
    cost_results = estimate_model(
        database,
        "summed_car_cost_mnl",
        models.loglogit(
            build_utilities(summed_car_cost=True),
            avail,
            choice,
        ),
    )
    cost_ll = log_likelihood(cost_results)

    # Nest scales for the active and motorised groups, starting near 1.
    mu_active = Beta("MU_ACTIVE", 1, 0.1, None, 0)
    mu_motor = Beta("MU_MOTOR", 1, 0.1, None, 0)
    # Two nests are required: active modes and motorised modes.
    nests = NestsForNestedLogit(
        choice_set=list(ALTERNATIVES.values()),
        tuple_of_nests=(
            OneNestForNestedLogit(
                nest_param=mu_active,
                # Walk and Cycle share the active nest.
                list_of_alternatives=[
                    ALTERNATIVES["Walk"],
                    ALTERNATIVES["Cycle"],
                ],
                name="Active",
            ),
            OneNestForNestedLogit(
                nest_param=mu_motor,
                # PT and Car share the motorised nest.
                list_of_alternatives=[ALTERNATIVES["PT"], ALTERNATIVES["Car"]],
                name="Motorized",
            ),
        ),
    )
    # Estimate Nested Logit with the same utilities as the Base MNL.
    nested_results = estimate_model(
        database,
        "active_motorized_nested_logit",
        models.lognested(base_utilities, avail, nests, choice),
    )
    nested_ll = log_likelihood(nested_results)

    # Calculate the market-share-only null log likelihood.
    # All observations are available here, but the calculation remains general.
    null_ll = float(-np.log(df[["AV_WALK", "AV_CYCLE", "AV_PT", "AV_CAR"]].sum(axis=1)).sum())
    # Count the fitted Base MNL parameters for adjusted rho-squared.
    base_parameter_count = len(base_results.get_beta_values())
    # Rho-squared is the proportional improvement over the null model.
    rho_squared = 1 - base_ll / null_ll
    # Adjusted rho-squared penalizes each estimated model parameter.
    adjusted_rho_squared = 1 - (base_ll - base_parameter_count) / null_ll
    # Compare the full MNL against the three restricted/nested specifications.
    generic_lr, generic_p = likelihood_ratio(base_ll, generic_ll, 3)
    cost_lr, cost_p = likelihood_ratio(base_ll, cost_ll, 2)
    nested_lr, nested_p = likelihood_ratio(nested_ll, base_ll, 2)

    # Assemble one comparison table containing LL, fit, LR, and p-values.
    comparison = pd.DataFrame(
        [
            {
                "Specification": "Base MNL",
                "N": len(df),
                "Parameters": base_parameter_count,
                "Null LL": null_ll,
                "Final LL": base_ll,
                "Rho-squared": rho_squared,
                "Adjusted rho-squared": adjusted_rho_squared,
                # The Base MNL is not tested against a further restricted model.
                "LR statistic": np.nan,
                "df": np.nan,
                "p-value": np.nan,
            },
            {
                "Specification": "Generic travel time MNL",
                "N": len(df),
                "Parameters": len(generic_results.get_beta_values()),
                "Null LL": null_ll,
                "Final LL": generic_ll,
                "Rho-squared": 1 - generic_ll / null_ll,
                "Adjusted rho-squared": 1
                - (generic_ll - len(generic_results.get_beta_values())) / null_ll,
                "LR statistic": generic_lr,
                # Three alternative-specific TT parameters are replaced by one.
                "df": 3,
                "p-value": generic_p,
            },
            {
                "Specification": "Summed car cost MNL",
                "N": len(df),
                "Parameters": len(cost_results.get_beta_values()),
                "Null LL": null_ll,
                "Final LL": cost_ll,
                "Rho-squared": 1 - cost_ll / null_ll,
                "Adjusted rho-squared": 1
                - (cost_ll - len(cost_results.get_beta_values())) / null_ll,
                "LR statistic": cost_lr,
                # Three separate car-cost parameters are replaced by one.
                "df": 2,
                "p-value": cost_p,
            },
            {
                "Specification": "Active vs motorized nested logit",
                "N": len(df),
                "Parameters": len(nested_results.get_beta_values()),
                "Null LL": null_ll,
                "Final LL": nested_ll,
                "Rho-squared": 1 - nested_ll / null_ll,
                "Adjusted rho-squared": 1
                - (nested_ll - len(nested_results.get_beta_values())) / null_ll,
                "LR statistic": nested_lr,
                # The nested test adds two nest-scale restrictions/parameters.
                "df": 2,
                "p-value": nested_p,
            },
        ]
    )
    # Save the comparison with four decimal places to the required location.
    comparison.to_csv(
        OUTPUT_DIR / "model_comparison.csv",
        index=False,
        float_format="%.4f",
    )

    # Convert fitted Base MNL coefficients into a plain Python dictionary.
    beta_values = {name: float(value) for name, value in base_results.get_beta_values().items()}
    # JSON allows the intervention teams to load coefficients without re-estimation.
    with (OUTPUT_DIR / "base_model_betas.json").open("w", encoding="utf-8") as beta_file:
        json.dump(beta_values, beta_file, indent=2, sort_keys=True)
        beta_file.write("\n")
    # Export coefficients, standard errors, t-statistics, and PT values of time.
    export_parameter_table(base_results, beta_values)

    # Print the observed overall and subgroup mode shares.
    print("Observed mode shares:")
    print(share_table(df).to_string(index=False, float_format=lambda value: f"{value:.4f}"))
    for group in ("AGE_GROUP", "INCOME_GROUP"):
        print(f"\nObserved mode shares by {group}:")
        print(
            share_table(df, group).to_string(
                index=False,
                float_format=lambda value: f"{value:.4f}",
            )
        )
    # Print the final model-comparison table for immediate review.
    print("\nModel comparison:")
    print(comparison.to_string(index=False, float_format=lambda value: f"{value:.4f}"))

    # Return data and key fitted values for assertions and optional reuse.
    return df, {
        "null_ll": null_ll,
        "base_ll": base_ll,
        "base_betas": beta_values,
        "nested_betas": nested_results.get_beta_values(),
    }


if __name__ == "__main__":
    # Run the complete workflow when this file is executed directly.
    df, fitted = main()
    # Confirm the mean-imputed analysis retains all 10,000 observations.
    assert len(df) == 10_000
    # Confirm no missing values remain after the shared preparation step.
    assert df.isna().sum().sum() == 0
    # Confirm the null-model log likelihood is within the requested tolerance.
    assert abs(fitted["null_ll"] - (-13_862.9436)) < 1e-3
    # Confirm the Base MNL final log likelihood is within the requested tolerance.
    assert abs(fitted["base_ll"] - (-7_949.7069)) < 1e-3
    # Confirm the PT waiting-time coefficient is the expected fitted value.
    assert abs(fitted["base_betas"]["B_WT_PT"] - (-0.0447)) < 1e-3
    # Confirm the PT fare coefficient is the expected fitted value.
    assert abs(fitted["base_betas"]["B_FARE_PT"] - (-0.9544)) < 1e-3
