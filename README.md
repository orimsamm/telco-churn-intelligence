# A Complete ETL and Business Intelligence Project on Telco Customer Churn

From Data Extraction with the Kaggle API to Descriptive Dashboards and Predictive Modeling in AWS Using Python, S3, and QuickSight

## Table of Contents
- [Overview](#overview)
- [Tools and Technologies](#tools-and-technologies)
- [Project Structure](#project-structure)
- [ETL Process](#etl-process)
- [Descriptive Analysis](#descriptive-analysis)
- [Predictive Analysis](#predictive-analysis)
- [AWS Integration](#aws-integration)
- [Final Deliverables](#final-deliverables)
- [How to Run Locally](#how-to-run-locally)

## Overview

This project explores customer churn in a telecom company using a full-stack BI approach:

- Extracted data from Kaggle using CLI
- Transformed and engineered features in Python
- Conducted descriptive analysis in AWS QuickSight
- Built and evaluated predictive models in Python
- Uploaded results to S3 and visualized predictions

## Tools and Technologies

- **Languages**: Python (Pandas, Scikit-learn)
- **Cloud**: AWS S3, AWS QuickSight
- **Data Source**: Kaggle (Telco Customer Churn)
- **Visualization**: AWS QuickSight
- **Version Control**: Git & GitHub

## Project Structure

```
telco_churn_project/
│
├── data/                      # Raw and cleaned CSVs
├── scripts/                   # Python scripts for preprocessing and modeling
├── Visuals/                   # All generated visualizations
└── README.md                  # Project summary and insights
```

## ETL Process

- Loaded Telco churn data via Kaggle API
- Cleaned missing values and formatted categories
- Engineered tenure groups, monthly charge bins
- Saved transformed dataset as `clean_telco.csv`

## Descriptive Analysis

### Churn by Contract Type
![Churn by Contract Type](Visuals/churn_by_contract_type.png)
Customers on month-to-month contracts had the highest churn. Long-term contracts (One year, Two year) showed better retention.

### Churn by Internet Service
![Churn by Internet Service](Visuals/churn_by_internet_service.png)
Fiber optic customers are more likely to churn, while customers with no internet service rarely churn.

### Churn by Tenure Group
![Churn by Tenure Group](Visuals/churn_by_tenure_group.png)
New customers (0–12 months) have the highest churn rate. Churn rate significantly drops with longer tenure.

### Churn by Monthly Charges
![Churn by Monthly Charges](Visuals/churn_by_monthly_charges.png)
Customers paying between $61–$90 churned the most. Lower churn is observed at the lowest and highest charge segments.

### Churn Percent by Contract & Gender
![Churn Percent by Contract and Gender](Visuals/churn_percent_by_contract_and_gender.png)
Month-to-month contract users have the highest churn for both genders. Female customers had slightly higher churn in general.

### Churn by Payment Method
![Churn by Payment Method](Visuals/churn_by_payment_method.png)
Electronic check users had significantly higher churn than those using credit card or bank transfer.

## Predictive Analysis

### Predicted Churn by Contract Type
![Predicted Churn by Contract Type](Visuals/avg_predicted_churn_by_contract.png)
Random Forest model predicts higher churn likelihood for short-term contracts — aligned with actual churn behavior.

### RF Predicted Churn by Monthly Group
![RF Predicted Churn by Monthly Group](Visuals/avg_rf_churn_by_monthly_charge_groups.png)
Customers with lower monthly charges are predicted to churn less than those with mid-range charges.

### RF Tenure Trend
![RF Tenure Trend](Visuals/churn_prediction_tenure_trend.png)
Model shows a clear decline in churn probability as tenure increases, supporting earlier descriptive insight.

### Confusion Matrix
![Confusion Matrix](Visuals/confusion_matrix_rf.png)
Most churners were misclassified as non-churn (high false negatives), suggesting model needs tuning or more features.

### RF Internet Churn
![RF Internet Churn](Visuals/predicted_by_internet_actual_status_rf.png)
Predicted churn by internet type aligns closely with actual behavior. DSL users show the highest predicted churn.

## AWS Integration

- Cleaned data and model results were uploaded to **Amazon S3**
- All dashboards created in **Amazon QuickSight**
- Project replicable via CLI and cloud tools

## Final Deliverables

- ✅ Clean dataset
- ✅ Jupyter modeling script
- ✅ QuickSight dashboard visuals
- ✅ GitHub-ready documentation

## How to Run Locally

1. Clone the repo
2. Navigate to `scripts/` and run:
   ```bash
   python churn_modeling.py
   ```
3. Outputs will be saved in `/data` and `/Visuals`
4. Upload to AWS S3 or QuickSight as needed