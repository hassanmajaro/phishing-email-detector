# feature_extractor.py
# This script handles feature extraction from email content using TF-IDF.

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

# Clean and combine subject and body into a single text column
def combine_text(df):
    # Fill NaN values with empty strings just in case
    df['subject'] = df['subject'].fillna('')
    df['body'] = df['body'].fillna('')

    # Combine subject and body into a new column called 'full_text'
    df['full_text'] = df['subject'] + ' ' + df['body']
    return df

# Extract TF-IDF features from the combined text
def extract_features(df, save_vectorizer=True):
    # Create a new TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english', max_features=3000)

    # Fit and transform the full_text column
    X = vectorizer.fit_transform(df['full_text'])

    # Save the vectorizer to disk for use during prediction
    if save_vectorizer:
        vec_path = os.path.join('models', 'tfidf_vectorizer.pkl')
        joblib.dump(vectorizer, vec_path)

    return X, df['label']
