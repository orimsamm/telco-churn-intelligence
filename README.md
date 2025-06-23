# Telco Customer Churn Project

From Kaggle CLI Extraction to AWS BI Reporting and Machine Learning Prediction

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

This project explores customer churn patterns in a telecom company. It combines cloud-based visualization with machine learning models to extract insights and predict churn behavior.

We used a structured pipeline:
- Extracted data using Kaggle CLI
- Cleaned and engineered features with Python
- Uploaded data to Amazon S3 using manifest files
- Visualized churn insights with AWS QuickSight
- Built machine learning models (Random Forest, Logistic Regression)
- Evaluated churn prediction accuracy and model performance

## Tools and Technologies

- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- AWS S3, AWS QuickSight
- Git and GitHub
- Kaggle CLI, JSON Manifest

## Project Structure

```
telco_churn_project/
├── Data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   ├── processed_telco.csv
│   ├── predicted_results.csv
│   ├── combined_churn_predictions.csv
├── Scripts/
│   ├── download_telco.py
│   ├── preprocess_telco.py
│   ├── train_model.py
│   ├── merge_and_export.py
│   ├── manifests/*.json
├── Visuals/
│   └── *.png
└── README.md
```

## ETL Process

### 1. Data Extraction

Kaggle CLI was used to download the dataset:

```bash
pip install kaggle
kaggle datasets download -d blastchar/telco-customer-churn
unzip telco-customer-churn.zip
```

### 2. Data Cleaning

- Standardized column names
- Converted TotalCharges to float
- Handled missing values and dropped duplicates

### 3. Feature Engineering

- Created tenure groups and charge bins
- Encoded churn as binary
- Prepared for machine learning input

### 4. File Exports

- `processed_telco.csv`: Cleaned version
- `predicted_results.csv`: Prediction + features
- `combined_churn_predictions.csv`: Final merged output

### 5. S3 Upload and Manifest

Data was uploaded to Amazon S3 using manifest files:

```json
{
  "fileLocations": [{"URIs": ["s3://bucket/combined_churn_predictions.csv"]}],
  "globalUploadSettings": {
    "format": "CSV", "delimiter": ",", "textqualifier": """, "containsHeader": "true"
  }
}
```

## Descriptive Analysis

### Churn by Contract Type
**Visual Type:** Bar Chart  
**Insight:** 1,659 customers with month-to-month contracts churned, while only 174 with one-year and 63 with two-year contracts churned.  
**Interpretation:** Month-to-month plans present the highest churn risk. Longer contracts significantly improve retention, suggesting customer commitment duration is a strong churn factor.

### Churn by Internet Service
**Visual Type:** Bar Chart  
**Insight:** 1,309 fiber optic customers churned versus 459 DSL and 110 with no internet service.  
**Interpretation:** Fiber optic customers show higher churn, possibly due to service reliability or pricing issues. This group should be a focus for quality and support improvements.

### Churn by Tenure Group
**Visual Type:** Bar Chart  
**Insight:** Most churn occurred in the 0–12 month range, accounting for over 1,000 churned users.  
**Interpretation:** New users are most at risk. Early-stage customer experience strategies are critical for improving retention in the first year.

### Churn by Monthly Charges
**Visual Type:** Histogram  
**Insight:** Customers paying $61–$90 per month showed the highest churn counts, while lower and higher brackets had less.  
**Interpretation:** Mid-range pricing may reflect a perceived lack of value. Tailored offers or added benefits could reduce churn in this billing range.

### Churn Percent by Contract & Gender
**Visual Type:** Grouped Bar Chart  
**Insight:** Female customers on month-to-month contracts had a churn rate of 43.74%.  
**Interpretation:** While gender differences are slight, contract type remains dominant. Gender-based behavioral analysis may enhance targeting.

### Churn by Payment Method
**Visual Type:** Bar Chart  
**Insight:** Customers paying by electronic check made up the largest share of churners at 1,074 users.  
**Interpretation:** Electronic check usage may correlate with less engagement or higher financial risk. Encouraging more reliable payment methods could stabilize retention.

---

## Predictive Analysis

### Average Predicted Churn by Contract Type
**Visual Type:** Bar Chart  
**Insight:** Month-to-month customers had a predicted churn rate of 0.18, one-year customers 0.19, and two-year customers 0.20.  
**Interpretation:** The increase in predicted churn for longer contracts is unexpected. It may indicate dissatisfaction over time among loyal customers, warranting deeper lifecycle analysis.

### Predicted Churn by Monthly Charge Groups
**Visual Type:** Horizontal Bar Chart  
**Insight:** Customers paying under $10 had a predicted churn rate of 0.18; those paying more had a rate of 0.20.  
**Interpretation:** Higher bills may cause dissatisfaction or cost sensitivity. Loyalty rewards or bundling might help retain high-value users.

### Churn Prediction Trend Across Tenure (3-Month Bins)
**Visual Type:** Line Chart  
**Insight:** Churn prediction starts near 0.2 for new customers and steadily declines as tenure increases.  
**Interpretation:** Long-term customers are less likely to churn. Onboarding and early satisfaction programs are essential to improve early retention.

### Confusion Matrix - Actual vs Predicted Churn (Random Forest)
**Visual Type:** Table  
**Insight:** The model correctly predicted 4,972 non-churners and only 65 churners. It misclassified 1,804 churners and 202 non-churners.  
**Interpretation:** The model struggles with recall for churners. Addressing class imbalance or adding features (e.g., service complaints, usage history) may improve sensitivity.

### Predicted Churn by Internet Service and Actual Churn Status
**Visual Type:** Stacked Bar Chart  
**Insight:** DSL users had the highest retention at 57.21%, while fiber users churned more at 48.57%.  
**Interpretation:** Although the model aligns with real churn trends, it may underestimate dissatisfaction in fiber customers. Additional service-related variables could improve accuracy.

## AWS Integration

- All cleaned and predicted datasets were uploaded to Amazon S3
- Dashboards were built in QuickSight using manifest-linked datasets
- This enabled seamless integration of Python models with cloud BI

## Final Deliverables

- Clean dataset: `processed_telco.csv`
- Model predictions: `predicted_results.csv`, `combined_churn_predictions.csv`
- Manifest files for S3 to QuickSight
- All visuals saved in `/Visuals/`
- Full documentation in `README.md`

## How to Run Locally

```bash
# Step 1: Install dependencies
pip install pandas scikit-learn kaggle

# Step 2: Download dataset
python Scripts/download_telco.py

# Step 3: Clean and process
python Scripts/preprocess_telco.py

# Step 4: Train model and export results
python Scripts/train_model.py
python Scripts/merge_and_export.py
```