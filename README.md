
#  A Complete ETL and Business Intelligence Project on Telco Customer Churn

From Data Extraction with the Kaggle API to Descriptive Dashboards and Predictive Modeling in AWS Using Python, S3, and QuickSight

---

##  Table of Contents

- [Overview](#overview)
- [Tools and Technologies](#tools-and-technologies)
- [Project Structure](#project-structure)
- [ETL Process](#etl-process)
- [Descriptive Analysis](#descriptive-analysis)
- [Predictive Analysis](#predictive-analysis)
- [AWS Integration](#aws-integration)
- [Final Deliverables](#final-deliverables)
- [How to Run Locally](#how-to-run-locally)

---

##  Overview

This project explores customer churn in a telecom company using a full-stack BI approach:

- Extracted data from Kaggle using CLI
- Transformed and engineered features in Python
- Conducted descriptive analysis in AWS QuickSight
- Built and evaluated predictive models in Python
- Uploaded results to S3 and visualized predictions

---

##  Tools and Technologies

- **Languages**: Python (Pandas, Scikit-learn)
- **Cloud**: AWS S3, AWS QuickSight
- **Visualization**: QuickSight
- **Data Source**: Kaggle (Telco Churn Dataset)
- **Other**: Kaggle CLI, Jupyter Notebook

---

##  Project Structure

```
├── ETL/
│   ├── telco_etl.ipynb
├── Visuals/
│   ├── churn_by_contract_type.png
│   ├── churn_by_tenure_group.png
│   ├── churn_by_monthly_charges.png
│   ├── random_forest_confusion_matrix.png
│   ├── feature_importance.png
├── predicted_results.csv
├── README.md
```

---

##  ETL Process

### Step 1: Install Required Packages

```bash
pip install kaggle pandas scikit-learn boto3
```

### Step 2: Configure Kaggle CLI

- Download your `kaggle.json` key from Kaggle account settings.
- Place it in the correct location:

```bash
mkdir ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### Step 3: Download Dataset from Kaggle

```bash
kaggle datasets download -d blastchar/telco-customer-churn
unzip telco-customer-churn.zip
```

### Step 4: Preprocess in Python

- Remove duplicates
- Handle missing values
- Encode categorical variables
- Engineer new features like `TenureGroup`, `TotalServices`

### Step 5: Save and Upload Cleaned Data to S3

- Save as `predicted_results.csv`
- Use `boto3` to upload

```python
import boto3

s3 = boto3.client('s3')
s3.upload_file("predicted_results.csv", "your-bucket-name", "predicted_results.csv")
```

### Step 6: Generate Manifest File

This manifest is used for QuickSight:

```json
{
  "fileLocations": [{
    "URIs": ["s3://your-bucket-name/predicted_results.csv"]
  }],
  "globalUploadSettings": {
    "format": "CSV",
    "delimiter": ",",
    "textqualifier": """,
    "containsHeader": "true"
  }
}
```

---

##  Descriptive Analysis

### Churn by Contract Type

![Churn by Contract Type](Visuals/churn_by_contract_type.png)

**Insight:**  
> Month-to-month contracts show the **highest churn at 43.2%**, versus **11.5%** (one-year) and **2.9%** (two-year). Longer contracts reduce churn significantly.

---

### Churn by Tenure Group

![Churn by Tenure Group](Visuals/churn_by_tenure_group.png)

**Insight:**  
> **52.5%** of customers in their **first 3 months** churn. Churn declines steadily beyond 12 months, reaching below **8%** after 24 months.

---

### Churn by Monthly Charges

![Churn by Monthly Charges](Visuals/churn_by_monthly_charges.png)

**Insight:**  
> Churn is **38.9%** for those paying over $80/month, but only **14.3%** for customers paying under $40/month. High charges may push customers away.

---

##  Predictive Analysis

### Confusion Matrix - Random Forest

![Random Forest Confusion Matrix](Visuals/random_forest_confusion_matrix.png)

**Insight:**  
> The model achieved an **accuracy of 80.1%**, correctly identifying **204 churns** and **964 non-churns**. However, **137 churners** were missed.

---

### Feature Importance

![Feature Importance](Visuals/feature_importance.png)

**Insight:**  
> **Contract**, **Tenure**, **Monthly Charges**, and **Internet Service** are the most important predictors of churn.

---

##  AWS Integration

- Uploaded cleaned data and prediction results to **Amazon S3**
- Created a **manifest file** for QuickSight integration
- Used **QuickSight dashboards** for visualization of churn insights

---

##  Final Deliverables

- Cleaned dataset: `predicted_results.csv`
- Visualizations in `Visuals/` folder
- Predictive models: Random Forest, Logistic Regression (tested)
- Insightful README and PDF for documentation

---

##  How to Run Locally

1. Clone the repo  
2. Install dependencies  
3. Run `telco_etl.ipynb`  
4. Upload final CSV to your S3 bucket  
5. Connect S3 to QuickSight via manifest  
6. Explore insights via dashboards

---
