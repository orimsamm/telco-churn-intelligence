
# Telco Customer Churn Project

## Overview
This project explores customer churn in a telecom company using a full-stack Business Intelligence approach. It combines ETL, cloud-based analytics, and predictive modeling to uncover why customers leave and to forecast future churn risk.

---

## Tools and Technologies
- **Languages**: Python (Pandas, Scikit-learn)
- **Cloud**: AWS S3, Amazon QuickSight
- **Visualization**: AWS QuickSight
- **Data Source**: Kaggle (Telco Customer Churn)
- **Version Control**: Git & GitHub

---

## Project Structure
```
telco_churn_project/
│
├── Data/                       # Raw and processed datasets
├── Scripts/                    # Python scripts for ETL and ML
├── Visuals/                    # Saved images from QuickSight
├── Docs/                       # Optional reports
├── README.md                   # This file
```

---

## ETL Process

### 1. Extract
- Install Kaggle:  
  ```bash
  pip install kaggle
  ```
- Place `kaggle.json` in `~/.kaggle/` and set permissions:
  ```bash
  chmod 600 ~/.kaggle/kaggle.json
  ```
- Download the dataset using CLI:  
  ```bash
  kaggle datasets download -d blastchar/telco-customer-churn
  ```
- Unzip and move into `Data/`

### 2. Transform
- Remove missing values (`TotalCharges`)
- Convert `SeniorCitizen` to binary
- Create grouped features:
  - `TenureGroup`: Binned into 12-month ranges
  - `MonthlyChargeGroup`: Low, Medium, High

Script used: `preprocess_telco.py`

### 3. Load
- Final files saved to:
  - `processed_telco.csv`
  - `predicted_results.csv`
  - `combined_churn_predictions.csv`

- Each file is uploaded to S3 using corresponding manifest:
  - `telco_manifest.json`
  - `telco_pred_manifest.json`
  - `combined_churn_manifest.json`

---

## Descriptive Analysis

### 📊 Churn by Contract Type  
![Churn by Contract Type](Visuals/churn_by_contract_type.png)  
**Insight**: Customers on month-to-month contracts are far more likely to churn compared to those on one-year or two-year contracts. This indicates short-term customers may feel less committed or face service dissatisfaction early on.

---

### 📊 Churn by Internet Service  
![Churn by Internet Service](Visuals/churn_by_internet_service.png)  
**Insight**: Fiber optic users showed significantly higher churn rates, possibly due to pricing or reliability concerns. Those without internet rarely churn — often older or low-usage customers.

---

### 📊 Churn by Tenure Group  
![Churn by Tenure Group](Visuals/churn_by_tenure_group.png)  
**Insight**: The highest churn occurs within the first 12 months. Retention improves significantly for long-tenured customers, reinforcing the need for onboarding incentives and early engagement.

---

### 📊 Churn by Monthly Charges  
![Churn by Monthly Charges](Visuals/churn_by_monthly_charges.png)  
**Insight**: Customers paying $61–$90 churn the most. This price range might be perceived as poor value, possibly indicating a pricing-to-value mismatch.

---

### 📊 Churn Percent by Contract & Gender  
![Churn by Contract and Gender](Visuals/churn_by_contract_gender.png)  
**Insight**: Gender has little effect on churn, but month-to-month contracts drive churn across both groups. Slightly higher churn among female customers is observed, but likely not statistically significant.

---

### 📊 Churn by Payment Method  
![Churn by Payment Method](Visuals/churn_by_payment_method.png)  
**Insight**: Customers using electronic checks churn far more often than those using bank transfers or credit cards. This could reflect a tech-savvy but less financially stable demographic.

---

## Predictive Analysis

### 🤖 Predicted Churn by Contract Type  
![RF Churn by Contract Type](Visuals/predicted_churn_by_contract_type_rf.png)  
**Insight**: The Random Forest model predicted churn probability highest for month-to-month customers, confirming descriptive trends. Long-term contracts had minimal predicted churn.

---

### 🤖 RF Churn by Monthly Charges  
![RF Monthly Group](Visuals/predicted_churn_by_monthly_group_rf.png)  
**Insight**: Predictions peaked around $70–$90 range. Lower churn prediction was made for both high-end and low-end charge brackets, aligning with earlier analysis.

---

### 🤖 RF Tenure Trend  
![RF Tenure Trend](Visuals/rf_tenure_trend.png)  
**Insight**: A steady decrease in predicted churn as tenure increases. This validated the earlier tenure group trend and suggests customer loyalty strengthens with time.

---

### 🤖 Confusion Matrix  
![Confusion Matrix](Visuals/confusion_matrix_rf.png)  
**Insight**: The model had high true positives but also misclassified many churners as non-churners (false negatives). This indicates the need for feature refinement or deeper modeling.

---

### 🤖 RF Internet Type Prediction  
![RF Internet Type](Visuals/rf_internet_churn.png)  
**Insight**: DSL users surprisingly showed the highest predicted churn, while fiber optic churn was moderate. This may reflect satisfaction drop-offs in DSL users.

---

## AWS Integration
- Processed datasets uploaded to **Amazon S3**
- Dashboards created in **Amazon QuickSight**
- Manifest `.json` files used to point to specific CSVs for upload and refresh

---

## Final Deliverables
- ✅ `processed_telco.csv`
- ✅ `predicted_results.csv`
- ✅ `combined_churn_predictions.csv`
- ✅ Python scripts for download, preprocess, modeling
- ✅ All charts saved in `Visuals/`
- ✅ Complete README documentation

---

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/orimsamm/telco-churn-intelligence.git

# Move into scripts and run preprocessing
cd Scripts
python preprocess_telco.py
python train_model.py
```

---

## Author  
Samuel Orimogunje  
Master's in Management Information Systems  
Business Intelligence & Cloud Enthusiast

