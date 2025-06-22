import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate the Kaggle API
api = KaggleApi()
api.authenticate()

# Dataset details
dataset = 'blastchar/telco-customer-churn'
save_path = 'telco_data'

# Download and unzip the dataset into the project folder
api.dataset_download_files(dataset, path=save_path, unzip=True)

print(f"✅ Download complete! Dataset extracted to: ./{save_path}")
