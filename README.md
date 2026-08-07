# Advanced Multi-Disease Risk Prediction System

An AI-powered healthcare application that predicts the risk of multiple diseases using Machine Learning models. The system enables users to enter clinical and demographic information and receive instant disease risk predictions through a modern web interface.

---

## 🚀 Features

- Heart Disease Risk Prediction
- Diabetes Risk Prediction
- Thyroid Disease Prediction
- Stroke Risk Prediction
- Real-time Prediction Results
- Responsive React Frontend
- REST API Integration with Flask
- Multiple Machine Learning Model Comparison
- Feature Engineering & Data Preprocessing

---

## 🛠 Tech Stack

### Frontend
- React.js
- HTML5
- CSS3
- JavaScript

### Backend
- Flask
- Python

### Machine Learning
- Scikit-learn
- XGBoost
- Pandas
- NumPy

### Models Evaluated
- XGBoost
- Random Forest
- Support Vector Machine (SVM)
- Logistic Regression
- Multi-Layer Perceptron (MLP)
- Decision Tree

---

## 📂 Project Structure

```
Multi-Disease-Risk-Prediction/
│
├── frontend/
│   ├── public/
│   ├── src/
│   └── package.json
│
├── backend/
│   ├── app.py
│   ├── models/
│   ├── dataset/
│   ├── utils/
│   ├── requirements.txt
│   └── saved_models/
│
├── screenshots/
│
└── README.md
```

---

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Missing Value Handling
4. Feature Engineering
5. Feature Scaling
6. Model Training
7. Model Evaluation
8. Model Selection
9. Model Deployment using Flask API

---

## 📊 Diseases Covered

| Disease | Prediction |
|----------|------------|
| ❤️ Heart Disease | Risk Classification |
| 🩸 Diabetes | Risk Classification |
| 🦋 Thyroid Disorder | Risk Classification |
| 🧠 Stroke | Risk Classification |

---

## 📈 Model Evaluation

The application evaluates multiple machine learning algorithms and selects the best-performing model based on validation metrics.

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

---

## 🌐 Application Workflow

```
User Input
      │
      ▼
React Frontend
      │
REST API Request
      │
      ▼
Flask Backend
      │
Data Preprocessing
      │
      ▼
Machine Learning Model
      │
Prediction
      │
      ▼
Prediction Result
```

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/tejal-29/Multi-Disease-Detection-System.git
cd Multi-Disease-Detection-System
```

---

### Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

Backend runs on:

```
http://localhost:5000
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm start
```

Frontend runs on:

```
http://localhost:3000
```

---

## 📷 Screenshots

Add screenshots here.

Example:

```
screenshots/
│
├── home.png
├── prediction.png
├── result.png
```

---

## 🔮 Future Enhancements

- User Authentication
- Patient History Management
- Medical Report Upload
- PDF Report Generation
- Doctor Dashboard
- Appointment Booking
- Cloud Deployment
- Explainable AI (SHAP/LIME)
- Model Monitoring
- Multi-language Support
