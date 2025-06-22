import pandas as pd

# Load processed feature data
features_df = pd.read_csv("./Data/processed_telco.csv")

# Load model prediction results
predictions_df = pd.read_csv("./Data/predicted_results.csv")

# Merge side-by-side
merged_df = pd.concat([features_df.reset_index(drop=True), predictions_df], axis=1)

# Save to new CSV
merged_df.to_csv("./Data/combined_churn_predictions.csv", index=False)

print("Merge complete. File saved as 'combined_churn_predictions.csv'")
