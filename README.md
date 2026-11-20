# CIVE70118 Coursework - Public Transport Demand Model

Python analysis repository for Imperial College London's CIVE70118/CIVE70016 coursework. The project uses a stated discrete-choice dataset of 10,000 work trips to estimate multinomial logit and nested logit models, then evaluates public-transport policy interventions.

## Coursework topic

**Topic 12:** Shift car-based travellers towards public transport by:

1. Increasing public-transport service frequency, represented by a reduction in waiting time.
2. Subsidising public-transport tickets, represented by a reduction in fare.

The analysis investigates impacts across age and income groups.

## Repository structure

```text
01_prepare_data.py  Shared dataset loading and preparation
02_base_case.py     Base MNL estimation and model comparison
03_intervention_1.py Public-transport frequency intervention (in progress)
04_intervention_2.py Public-transport fare intervention (in progress)
data/               Survey data
docs/               Coursework brief, dataset dictionary, and meeting notes
outputs/            Estimated model outputs and comparison tables
requirements.txt    Python dependencies
```

## Data preparation

`01_prepare_data.py` provides `load_clean_data()`, which:

- Loads `data/Dataset_1_2026.csv`.
- Trims and validates string and numeric columns.
- Renames `CAR OWNERSHIP` to `CAR_OWNERSHIP`.
- Replaces missing `TT_WALK` values with the sample mean.
- Adds `FEMALE`, `AGE_GROUP`, and `INCOME_GROUP` columns.
- Checks required columns and subgroup ranges.

The subgroup ranges are:

- Age: 18-29, 30-44, 45-59, and 60-70.
- Income: 10k-32k, 33k-55k, 56k-78k, and 79k-100k (GBP).

The dataset dictionary is available in [docs/Dataset 1 Dictionary 2026.md](docs/Dataset%201%20Dictionary%202026.md).

## Setup

Use Python 3.10 or later and create a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the base model

From the repository root:

```powershell
python 02_base_case.py
```

The script:

- Estimates the full four-mode base multinomial logit model.
- Estimates generic travel-time and summed car-cost restricted specifications.
- Estimates an active (walk/cycle) versus motorised (PT/car) nested logit model.
- Calculates likelihood-ratio tests and goodness-of-fit measures.
- Reports observed mode shares overall and by age and income group.
- Runs consistency assertions for the prepared data and key fitted coefficients.

## Outputs

Running `02_base_case.py` writes the following files to `outputs/`:

- `base_model_params.csv` - coefficients, standard errors, t-statistics, and public-transport values of time.
- `base_model_betas.json` - fitted coefficients used by the intervention scripts.
- `model_comparison.csv` - log likelihoods, rho-squared measures, likelihood-ratio tests, and p-values.

The intervention scripts currently contain TODO starters for the two policy experiments. They load the prepared data and base-model coefficients, but have not yet implemented scenario utilities or market-share calculations.

## Model overview

The four alternatives are:

| Mode | CHOSEN_MODE code |
| --- | --- |
| Walk | 1 |
| Cycle | 2 |
| Public transport | 3 |
| Car | 4 |

Walk is the reference alternative. The utility specifications include alternative-specific constants, travel attributes, built-environment indices, socio-demographic terms, and car ownership where applicable.
