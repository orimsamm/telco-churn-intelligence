import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the cleaned data I just saved
df = pd.read_csv('./Data/processed_telco.csv')

# Split the data — target is Churn, rest are features
X = df.drop('Churn', axis=1)
y = df['Churn']

# I’ll use 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# First model — Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)

print("Logistic Regression Results")
print(confusion_matrix(y_test, log_preds))
print(classification_report(y_test, log_preds))

# Second model — Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

print("Random Forest Results")
print(confusion_matrix(y_test, rf_preds))
print(classification_report(y_test, rf_preds))

# Save predictions with Customer index, actual churn, predicted churn
results = pd.DataFrame({
    'ActualChurn': y_test,
    'LogisticPred': log_preds,
    'RandomForestPred': rf_preds
})

results.to_csv('./Data/predicted_results.csv', index=False)
print("Model predictions saved to 'predicted_results.csv'")
