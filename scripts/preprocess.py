# preprocess.py
# This script loads and prepares email data for feature extraction and training.

import pandas as pd
import os

# Load phishing and legit email datasets
def load_datasets():
    # Adjust file paths based on your actual structure
    phishing_path = os.path.join('data', 'phishing_emails.csv')
    legit_path = os.path.join('data', 'legit_emails.csv')
    
    # Read the CSVs into pandas DataFrames
    phishing_df = pd.read_csv(phishing_path)
    legit_df = pd.read_csv(legit_path)

    # Add a label column: 1 for phishing, 0 for legit
    phishing_df['label'] = 1
    legit_df['label'] = 0

    # Combine the datasets into one
    combined_df = pd.concat([phishing_df, legit_df], ignore_index=True)

    # Drop rows with any missing values (optional)
    combined_df.dropna(inplace=True)

    return combined_df
