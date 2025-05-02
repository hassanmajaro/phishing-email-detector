# predict.py
# This script loads the trained model and predicts if a given email is phishing.

import os
import joblib
from scripts.url_analyzer import extract_urls, score_url

# Load trained model and vectorizer from the models folder
model_path = os.path.join('models', 'phishing_model.pkl')
vectorizer_path = os.path.join('models', 'tfidf_vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Function to predict phishing or legit
def predict_email(subject, body):
    # Combine subject and body
    full_text = subject + " " + body

    # Vectorize text for ML model
    X_input = vectorizer.transform([full_text])

    # Predict using the trained model
    prediction = model.predict(X_input)

    # Extract and score URLs from the body
    urls = extract_urls(body)
    suspicious_urls = [url for url in urls if score_url(url) >= 2]

    # Return result and flagged URLs
    return {
        'verdict': "Phishing 🚨" if prediction[0] == 1 else "Legit ✅",
        'suspicious_urls': suspicious_urls
    }
