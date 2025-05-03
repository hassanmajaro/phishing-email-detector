# 🛡️ Phishing Email Detector

A machine learning-powered phishing detector that analyzes email content and identifies suspicious patterns, including malicious URLs.  
Built with 💻 Python, 🧠 scikit-learn, and 🌐 Flask.

---

## 🚀 Features

- ✅ Detects phishing vs legitimate emails
- 🔗 Extracts and analyzes suspicious URLs
- 🧠 Machine learning model (TF-IDF + Random Forest)
- 🌐 Web interface with light/dark mode toggle
- 🎨 Interactive, modern UI
- 🧰 Easy to retrain with your own dataset

---

## 📸 Screenshot

![phish](https://github.com/user-attachments/assets/9269ae0d-ee91-40f4-ac58-5957893ee5f2)


---

## 🏗️ File Structure

<pre>
  phishing_detector/
  ├── app/
  │ ├── detector_api.py       # Flask web app
  │ └── templates/index.html  # Frontend
  ├── data/                   # Email datasets
  ├── models/                 # Model + vectorizer (generated after training)
  ├── scripts/
  │ ├── train_model.py        # Train model
  │ ├── predict.py            # Predict phishing or legit
  │ ├── preprocess.py         # Load datasets
  │ ├── feature_extractor.py  # TF-IDF vectorization
  │ └── url_analyzer.py       # Suspicious URL detection
  ├── requirements.txt
  └── README.md
</pre>

---

## 🧪 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/hassanmajaro/phishing-email-detector.git
cd phishing-email-detector
````

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Datasets
Place your email in the data/ folder:
-  phishing_emails.csv
-  legit_emails.csv

### 4. Train the Model
```bash
python scripts/train_model.py
```

### 5. Run the Web App
```bash
python app/detector_api.py
```
Open in your browser: http://127.0.0.1:5000

---

## 📊 Sample Dataset Format
Both .csv files should have at least:
```csv
subject,body,from
"URGENT: Account Warning", "Click here: http://phish.com", "noreply@fakebank.com"
```

---

## 🤝 Contributing
Pull requests are welcome!

If you have feature suggestions or want to help improve detection, feel free to open an issue or PR

---

## 👨‍💻 Author
Majaro Hassan

Cybersecurity Enthusiast 

https://github.com/hassanmajaro



