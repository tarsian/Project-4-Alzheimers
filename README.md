# Project-4
<img src="https://capsule-render.vercel.app/api?type=waving&color=BDBDC8&height=150&section=header" />

[Project-4-Proposal](https://docs.google.com/document/d/1wjlaXLGC6ZO0PcoKIO1drjRMGmiGWQUmc7J78Ze_ab0/edit)

# Alzheimer's Disease Prediction

## Project Overview
This project aims to predict Alzheimer's Disease using machine learning models.

## Data [Link](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset)
The dataset used in this project includes demographic, clinical, and lifestyle information.

## Models
Three models were implemented:
- Random Forest
- Decision Tree
- Logistic Regression

## Initial Results
- **Random Forest**
  - Accuracy: 95.43%
  - AUC: 0.9640

- **Decision Tree**
  - Accuracy: 90.87%
  - AUC: 0.8928

- **Logistic Regression**
  - Accuracy: 84.38%
  - AUC: 0.8975

## Optimized Results

### Random Forest
- **Best Parameters**: {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
- **Cross-validation Accuracy**: 93.18%
- **Test Accuracy**: 95.19%
- **Confusion Matrix**:

|          | Predicted Negative | Predicted Positive |
|----------|--------------------|--------------------|
| Actual Negative | 283                | 5                  |
| Actual Positive | 15                 | 113                |

- **Classification Report**:

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0.0   | 0.95      | 0.98   | 0.97     | 288     |
| 1.0   | 0.96      | 0.88   | 0.92     | 128     |
| **Accuracy** |       |        |          | **0.95** |
| **Macro Avg** | 0.95      | 0.93   | 0.94     | 416     |
| **Weighted Avg** | 0.95      | 0.95   | 0.95     | 416     |

### Decision Tree
- **Best Parameters**: {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10}
- **Cross-validation Accuracy**: 91.98%
- **Test Accuracy**: 94.47%
- **Confusion Matrix**:

|          | Predicted Negative | Predicted Positive |
|----------|--------------------|--------------------|
| Actual Negative | 280                | 8                  |
| Actual Positive | 15                 | 113                |

- **Classification Report**:

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0.0   | 0.95      | 0.97   | 0.96     | 288     |
| 1.0   | 0.93      | 0.88   | 0.91     | 128     |
| **Accuracy** |       |        |          | **0.94** |
| **Macro Avg** | 0.94      | 0.93   | 0.93     | 416     |
| **Weighted Avg** | 0.94      | 0.94   | 0.94     | 416     |

## Usage
To run the project, follow these steps:
1. Clone the repository
2. Install the required packages
3. Run the `main.py` script

<img src="https://capsule-render.vercel.app/api?type=waving&color=BDBDC8&height=150&section=footer" />
