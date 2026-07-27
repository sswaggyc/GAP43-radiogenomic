# Model card

## Models

### Primary SVM model

- Task: binary estimation of GAP43-high versus GAP43-low expression status
- Algorithm: linear support vector machine with balanced class weights and probability calibration
- Output: predicted probability of GAP43-high status, defined as the radiomics score (RS)
- Features: two CE-T1WI-derived radiomic features

### Logistic-regression comparator

- Task: the same binary classification task using the same two features
- Algorithm: unpenalized logistic regression with balanced class weights
- Output: predicted probability of GAP43-high status, reported as a comparator rather than the manuscript RS

## Development population

Both models were fitted using 56 patients with surgically resected lung adenocarcinoma brain metastases and paired RNA-sequencing and CE-T1WI data.

## Comparative interpretation

The models showed comparable predictive performance. The SVM did not demonstrate a statistically significant or clinically meaningful improvement over LR. The SVM is retained as the primary RS-generating model to maintain consistency with the original analytical framework and downstream prognostic analyses; this designation should not be interpreted as evidence of superiority.

## Appropriate use

- Reproduction of the published feature-level models
- Independent validation using compatible radiomic features
- Methodological comparison of SVM and LR

## Inappropriate use

- Stand-alone treatment selection
- Automated changes to surveillance intensity
- Replacement of tissue-based molecular assessment
- Use without confirming compatible feature-extraction and harmonization procedures

## Known limitations

- Small, single-center development cohort
- No independent cohort with paired imaging and GAP43 RNA expression
- Sensitivity to acquisition, segmentation, feature extraction, and harmonization differences
- No prospectively validated clinical decision threshold
