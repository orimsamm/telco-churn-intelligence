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

The project followed a structured ETL (Extract, Transform, Load) pipeline to prepare the Telco Customer Churn dataset for analysis and modeling.

### Extract
The raw Telco Churn dataset was sourced from Kaggle using the Kaggle API. It was downloaded into the /data directory using:

```
kaggle datasets download -d blastchar/telco-customer-churn
```

### Transform
Data transformations were performed using Python and Pandas:

- Handling Missing Values:
  - The TotalCharges column contained missing values. These were either removed or filled with zero based on context.
  - Rows with missing values in tenure or other critical fields were dropped.

- Data Type Conversion:
  - TotalCharges was converted from string to float.
  - SeniorCitizen was encoded from 0/1 to Yes/No to match other binary columns.

- Feature Engineering:
  - Tenure was grouped into 3-month intervals (0–3, 4–6, etc.) for better lifecycle analysis.
  - MonthlyCharges was bucketed into groups (<=30, 31–60, 61–90, >90).
  - The Churn column was encoded into binary: Yes = 1, No = 0.
  - Contract Type and Internet Service were retained as categorical features.

- Column Standardization:
  - All column headers were converted to lowercase and snake_case format for consistency.

The cleaned dataset was saved as:

```
data/clean_telco.csv
```

### Load
- The cleaned dataset was uploaded to Amazon S3 for secure cloud storage.
- AWS QuickSight connected directly to this file for dashboard creation.
- Python scripts also loaded this CSV for churn modeling and predictions.

## Descriptive Analysis

#### Churn by Contract Type

![Churn by Contract Type](Visuals/churn_by_contract_type.png)

**Visual Type:** Bar Chart  
**Insight:** Month-to-month users had the highest churn count (1.66K), while two-year users had the lowest (0.05K).  
**Interpretation:** Short-term contracts are a strong churn predictor. Incentivizing longer contracts may help reduce churn.

#### Churn by Internet Service

![Churn by Internet Service](Visuals/churn_by_internet_service.png)

**Visual Type:** Bar Chart  
**Insight:** Fiber optic users had the highest churn (1.3K), while DSL and No Internet users had significantly lower churn.  
**Interpretation:** Fiber users may be dissatisfied with service or pricing. This group should be prioritized for feedback and retention.

#### Churn by Tenure Group

![Churn by Tenure Group](Visuals/churn_by_tenure_group.png)

**Visual Type:** Bar Chart  
**Insight:** Most churn happens in the 0–12 month group (1.04K churned).  
**Interpretation:** New customers are the most vulnerable to churn. Onboarding and early engagement strategies are critical.

#### Churn by Monthly Charges

![Churn by Monthly Charges](Visuals/churn_by_monthly_charges.png)

**Visual Type:** Histogram  
**Insight:** Users paying between $61–$90 churn the most.  
**Interpretation:** This may indicate a price sensitivity zone. Targeted promotions or tiered pricing can reduce churn here.

#### Churn Percent by Contract & Gender

![Churn Percent by Contract and Gender](Visuals/churn_percent_by_contract_and_gender.png)

**Visual Type:** Grouped Bar Chart  
**Insight:** Month-to-month female users had the highest churn rate at 43.74%.  
**Interpretation:** While contract type is dominant, slight gender variations suggest deeper behavioral segmentation could help.

#### Churn by Payment Method

![Churn by Payment Method](Visuals/churn_by_payment_method.png)

**Visual Type:** Bar Chart  
**Insight:** Users paying via electronic check churn the most (1.07K).  
**Interpretation:** This method may be tied to less tech-savvy or lower-income segments. Consider targeted digital onboarding or switching incentives.

## Predictive Analysis

#### Average Predicted Churn by Contract Type

![Predicted Churn by Contract Type](Visuals/avg_predicted_churn_by_contract.png)

**Visual Type:** Bar Chart  
**Insight:** Month-to-month customers had a predicted churn rate of 0.18, one-year customers 0.19, and two-year 0.20.  
**Interpretation:** Unexpectedly, churn probability rises slightly with longer contracts. Explore if tenure length causes dissatisfaction later in the customer lifecycle.

#### Predicted Churn by Monthly Charge Groups

![RF Predicted Churn by Monthly Group](Visuals/avg_rf_churn_by_monthly_charge_groups.png)

**Visual Type:** Horizontal Bar Chart  
**Insight:** Customers paying less than $10 had a churn prediction of 0.18; those paying more had 0.20.  
**Interpretation:** Higher spenders might feel underserved or overcharged. Bundling extra features could improve retention.

#### Churn Prediction Trend Across Tenure (3-Month Bins)

![RF Tenure Trend](Visuals/churn_prediction_tenure_trend.png)

**Visual Type:** Line Chart  
**Insight:** Churn probability starts near 0.2 for new customers and decreases with tenure.  
**Interpretation:** Long-term users are more stable. Improving the first 3–6 months of user experience is key to long-term retention.

#### Confusion Matrix - Actual vs Predicted Churn (Random Forest)

![Confusion Matrix](Visuals/confusion_matrix_rf.png)

**Visual Type:** Matrix Table  
**Insight:** The model correctly predicted 4,972 non-churners and 65 churners. It missed 1,804 actual churners.  
**Interpretation:** The model has low recall for churners — possibly due to class imbalance. Techniques like SMOTE or more targeted features may improve accuracy.

#### Predicted Churn by Internet Service and Actual Churn Status

![RF Internet Churn](Visuals/predicted_by_internet_actual_status_rf.png)

**Visual Type:** Stacked Bar Chart  
**Insight:** DSL users had the highest predicted retention (57.21%), while fiber users churned almost as much as they stayed.  
**Interpretation:** The model underestimates fiber churn. DSL seems more stable, but further segmentation might reveal why fiber users are dissatisfied.

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