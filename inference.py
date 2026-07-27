"""Feature-level inference for the GAP43 radiogenomic models."""

from __future__ import annotations

import argparse
from pathlib import Path

import joblib
import pandas as pd


FEATURES = [
    "wavelet-HHH_firstorder_Skewness",
    "wavelet-HLL_glrlm_ShortRunEmphasis",
]

MODEL_FILES = {
    "svm": "Final_SVM_Model.joblib",
    "lr": "Final_Logistic_Regression_Model.joblib",
}


def load_model(model_name: str, repository_dir: Path):
    model_path = repository_dir / MODEL_FILES[model_name]
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return joblib.load(model_path)


def add_predictions(output: pd.DataFrame, features: pd.DataFrame, model_name: str, pipeline) -> None:
    probability = pipeline.predict_proba(features)[:, 1]
    predicted_class = pipeline.predict(features)

    if model_name == "svm":
        output["RS_probability_GAP43_high"] = probability
        output["SVM_predicted_GAP43_class"] = predicted_class
    else:
        output["LR_probability_GAP43_high"] = probability
        output["LR_predicted_GAP43_class"] = predicted_class


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Run the primary SVM model, the logistic-regression comparator, "
            "or both models using two pre-extracted radiomic features."
        )
    )
    parser.add_argument("--input", required=True, type=Path, help="CSV containing the two required feature columns.")
    parser.add_argument("--output", required=True, type=Path, help="Destination CSV for predictions.")
    parser.add_argument(
        "--model",
        choices=["svm", "lr", "both"],
        default="svm",
        help="Model to run. The default 'svm' returns the manuscript radiomics score (RS).",
    )
    args = parser.parse_args()

    data = pd.read_csv(args.input)
    missing = [feature for feature in FEATURES if feature not in data.columns]
    if missing:
        raise ValueError(f"Missing required feature columns: {missing}")
    if data[FEATURES].isna().any().any():
        raise ValueError("The required feature columns contain missing values.")

    repository_dir = Path(__file__).resolve().parent
    feature_data = data[FEATURES]
    output = data.drop(columns=FEATURES, errors="ignore").copy()

    requested_models = ["svm", "lr"] if args.model == "both" else [args.model]
    for model_name in requested_models:
        pipeline = load_model(model_name, repository_dir)
        add_predictions(output, feature_data, model_name, pipeline)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(args.output, index=False)
    print(f"Saved {len(output)} prediction(s) to {args.output}")


if __name__ == "__main__":
    main()
