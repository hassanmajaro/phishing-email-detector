# train_model.py
# This script trains a phishing email detection model using TF-IDF features.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Import helper scripts
from scripts.preprocess import load_datasets
from scripts.feature_extractor import combine_text, extract_features

# Load and combine the datasets (phishing + legit)
df = load_datasets()

# Combine subject and body into a single text column
df = combine_text(df)

# Extract features (X) and labels (y)
X, y = extract_features(df)

# Split the data into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize a RandomForest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate on test data
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save the trained model
model_path = os.path.join('models', 'phishing_model.pkl')
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
