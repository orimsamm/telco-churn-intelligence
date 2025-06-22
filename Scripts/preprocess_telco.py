import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load raw dataset
df = pd.read_csv('./Data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Drop customerID (not needed for modeling)
df.drop('customerID', axis=1, inplace=True)

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Fill missing TotalCharges with the median
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Convert Churn column to binary
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Keep these categorical columns as string labels
keep_as_string = [
    'Contract', 'PaymentMethod', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Partner', 'Dependents', 'PhoneService',
    'MultipleLines', 'gender', 'PaperlessBilling'
]

# Label encode only the object columns not in keep_as_string
cat_cols = df.select_dtypes(include='object').columns
cols_to_encode = [col for col in cat_cols if col not in keep_as_string]

le = LabelEncoder()
for col in cols_to_encode:
    df[col] = le.fit_transform(df[col])

# Normalize numeric features
scaler = StandardScaler()
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[num_cols] = scaler.fit_transform(df[num_cols])

# Save the processed dataset
df.to_csv('./Data/processed_telco.csv', index=False)

print("Preprocessing complete. File saved as 'processed_telco.csv'")
