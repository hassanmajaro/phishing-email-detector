# detector_api.py
# Flask API for phishing email prediction

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from scripts.predict import predict_email

# Create Flask application
app = Flask(__name__)

# Route for the home page that renders the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    subject = request.form['subject']
    body = request.form['body']

    result = predict_email(subject, body)

    return render_template(
        'index.html',
        prediction=result['verdict'],
        subject=subject,
        body=body,
        urls=result['suspicious_urls']
    )

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
