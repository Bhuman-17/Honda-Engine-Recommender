# 🧠 Honda Engine Recommendation System

![Flask](https://img.shields.io/badge/Framework-Flask-blue)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-brightgreen)
![License](https://img.shields.io/badge/License-MIT-orange)

An intelligent, ML-powered **Flask web application** that recommends the most suitable **Honda engine series and specifications** based on user-defined inputs such as fuel type, power requirement, engine type, and more.

---

## 🔍 Preview

### 🎛️ Input Form  
> Users select engine requirements using a structured dropdown interface.

![Input Form](https://raw.githubusercontent.com/Bhuman-17/Honda-Engine-Recommender/main/assets/input_form.png)

---

### 📊 Output Prediction + Top 3 Matches  
> Results page displays predicted **series**, detailed **specs**, and the **top 3 closest engine options**.

![Prediction Output](https://raw.githubusercontent.com/Bhuman-17/Honda-Engine-Recommender/main/assets/prediction_result.png)

---

### 📈 Dashboard (Power BI Analysis)  
> Embedded Power BI visuals give a breakdown of engine data across series, product types, and key features.

![Dashboard](https://raw.githubusercontent.com/Bhuman-17/Honda-Engine-Recommender/main/assets/dashboard.png)

---

### ❓ Why Honda  
> Informational section showcasing Honda's strengths, quality, and innovation.

![Why Honda Page](https://raw.githubusercontent.com/Bhuman-17/Honda-Engine-Recommender/main/assets/why_honda.png)

---

### 🔚 Homepage  
> Landing page welcoming users and guiding them through the recommendation process.

![Homepage](https://raw.githubusercontent.com/Bhuman-17/Honda-Engine-Recommender/main/assets/homepage.png)

---

## 💡 Key Features

- 🔍 Predicts **engine series** using a trained classification model.
- 📐 Predicts **specifications** (e.g. Bore, Stroke, Power, Oil Capacity) via regression.
- 🏆 Shows **top 3 engine recommendations** based on closest feature match.
- 📊 Integrated Power BI dashboard for engine insights.
- 🌐 Multi-page Flask interface with navigation between Home, Dashboard, and Recommender.

---

## 🧠 Tech Stack

| Component     | Technology                         |
|---------------|------------------------------------|
| Backend       | Flask                              |
| ML Models     | Random Forest (Classifier + Regressor) |
| Deployment    | Localhost / Web-hosted Flask App   |
| Frontend      | HTML, CSS (Jinja Templates)        |
| Visualisation | Power BI                           |
| Data Handling | Pandas, scikit-learn, joblib       |

---

## ⚙️ Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/Bhuman-17/Honda-Engine-Recommender.git
cd Honda-Engine-Recommender
````

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 📦 Requirements

```
flask
scikit-learn
pandas
numpy
joblib
flask-cors
```

---

## 📁 Project Structure

```
├── app.py
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── recommender.html
│   └── result.html
├── static/
│   └── style.css
├── models/
│   ├── best_regressor_model.joblib
│   ├── series_classifier_model.joblib
│   └── series_label_encoder.joblib
├── assets/
│   └── [screenshots]
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

* Add authentication and admin panel
* Save prediction history to a database
* Allow exporting recommendation reports
* Host on Render or Railway
