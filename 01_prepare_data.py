"""Shared data preparation for the base and intervention models."""

from pathlib import Path

import pandas as pd


DEFAULT_DATA_PATH = "data/Dataset_1_2026.csv"
AGE_GROUPS = ["18-29", "30-44", "45-59", "60-70"]
INCOME_GROUPS = ["10k-32k", "33k-55k", "56k-78k", "79k-100k"]


def load_clean_data(path: str | Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the trip dataset, impute walk time, and add subgroup columns."""
    data_path = Path(path)
    if not data_path.is_absolute():
        data_path = Path(__file__).resolve().parent / data_path

    df = pd.read_csv(data_path)
    df.columns = df.columns.str.strip()
    for column in df.select_dtypes(include="object"):
        df[column] = df[column].str.strip().replace("", pd.NA)
    df = df.rename(columns={"CAR OWNERSHIP": "CAR_OWNERSHIP"})

    required_columns = {
        "TT_WALK",
        "GENDER",
        "AGE",
        "INCOME",
        "CAR_OWNERSHIP",
    }
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing_columns)}")

    df["TT_WALK"] = pd.to_numeric(df["TT_WALK"], errors="raise")
    df["TT_WALK"] = df["TT_WALK"].fillna(df["TT_WALK"].mean())
    df["FEMALE"] = (df["GENDER"] == 2).astype(int)
    df["AGE_GROUP"] = pd.cut(
        df["AGE"],
        bins=[17, 29, 44, 59, 70],
        labels=AGE_GROUPS,
    )
    df["INCOME_GROUP"] = pd.cut(
        df["INCOME"],
        bins=[9, 32, 55, 78, 100],
        labels=INCOME_GROUPS,
    )

    if df[["TT_WALK", "AGE_GROUP", "INCOME_GROUP"]].isna().any().any():
        raise ValueError("Data contains missing walk times or values outside subgroup ranges.")
    return df
