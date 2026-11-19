"""Starter for the public-transport frequency intervention."""

import json
from importlib import import_module
from pathlib import Path

load_clean_data = import_module("01_prepare_data").load_clean_data


# TODO [Intervention 1]: Reduce WT_PT (increased PT service frequency) and evaluate market-share shifts across AGE_GROUP and INCOME_GROUP.
def main() -> None:
    df = load_clean_data()
    beta_path = Path(__file__).resolve().parent / "outputs" / "base_model_betas.json"
    with beta_path.open(encoding="utf-8") as beta_file:
        betas = json.load(beta_file)


if __name__ == "__main__":
    main()
