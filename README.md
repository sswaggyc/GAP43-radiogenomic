# GAP43 radiogenomic models

This repository provides the feature-level models used to estimate high GAP43 expression in surgically resected lung adenocarcinoma brain metastases.

- **Primary model:** linear support vector machine (SVM). Its predicted probability of GAP43-high status is the manuscript radiomics score (RS).
- **Transparent comparator:** unpenalized logistic regression (LR), evaluated using the same two features and cross-validation partitions.

The LR model is included to support interpretation and independent comparison. It does not replace the SVM-derived RS used in the downstream prognostic analyses.

## Intended use

The package is provided for research and independent validation. Neither model is a stand-alone clinical decision tool, and no prospectively validated treatment, surveillance, or molecular-testing threshold is defined.

## Required inputs

The inference script requires two radiomic features:

1. `wavelet-HHH_firstorder_Skewness`
2. `wavelet-HLL_glrlm_ShortRunEmphasis`

The values must be obtained using imaging preprocessing, segmentation, feature extraction, and harmonization procedures consistent with those described in the manuscript. This repository performs feature-level inference; it does not convert raw MRI and segmentation files into radiomic features.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run inference

Primary SVM model and manuscript RS:

```bash
python inference.py --input example_features.csv --output svm_predictions.csv --model svm
```

Logistic-regression comparator:

```bash
python inference.py --input example_features.csv --output lr_predictions.csv --model lr
```

Both models:

```bash
python inference.py --input example_features.csv --output both_predictions.csv --model both
```

For the SVM, `RS_probability_GAP43_high` is the fitted probability of GAP43-high status and is the manuscript RS. The LR probability is reported separately as `LR_probability_GAP43_high`.

## Model specifications

- `Final_SVM_Specification.json` reports the feature means, scaling divisors, linear SVM coefficients, intercept, hyperparameters, and probability-calibration parameters.
- `Final_Logistic_Regression_Specification.json` reports the corresponding LR coefficients, intercept, and preprocessing parameters.
- `MODEL_COMPARISON.md` summarizes the repeated nested cross-validation and participant-level paired comparison.

The `.joblib` files contain complete fitted scikit-learn pipelines, including `StandardScaler` and the relevant classifier.

## Reproducibility files

- `example_features.csv`: synthetic input. The commands above generate the corresponding output file locally.

## Data availability

No patient-level MRI, transcriptomic, clinical, or prediction data are included. Raw data are subject to institutional governance and patient-privacy restrictions.

## Limitations

The models were developed in a small, single-center radiogenomic cohort and require external validation. Scanner, acquisition, segmentation, feature-extraction, and harmonization differences may affect transportability.
