# 🏥 Medical Insurance Cost Prediction Dashboard

An end-to-end Machine Learning web application that predicts medical insurance charges based on customer demographics and health-related factors.

**Python | Streamlit | Scikit-Learn | Plotly | Linear Regression**

---

## 📌 Project Overview

Medical Insurance Cost Prediction Dashboard uses a trained Linear Regression model to estimate medical insurance charges based on user inputs such as age, gender, BMI, smoking status, number of children, and region.

The application provides:

* Real-time insurance cost prediction
* Risk level assessment (Low, Medium, High)
* Interactive data visualizations
* Dataset analytics dashboard
* Cloud deployment using Streamlit Community Cloud

---

## 🗂 Project Structure

```text
insurance-cost-prediction/
├── app.py
├── insurance.csv
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── linear_regression.ipynb
```

---

## ⚙️ Features Used

| Feature          | Type        |
| ---------------- | ----------- |
| Age              | Numeric     |
| Gender           | Categorical |
| BMI              | Numeric     |
| Children         | Numeric     |
| Smoker           | Binary      |
| Region           | Categorical |
| Obesity Category | Binary      |

---

## 🤖 Model Information

### Algorithm Used

* Linear Regression

### Preprocessing

* Data Cleaning
* Feature Engineering
* Label Encoding
* Standard Scaling
* Train-Test Split

### Evaluation Metrics

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

---

## 📊 Dashboard Features

### Prediction Module

* Insurance cost prediction
* Risk level classification
* Interactive user inputs

### Analytics Dashboard

* Age vs Insurance Charges
* BMI vs Insurance Charges
* Smoker vs Non-Smoker Analysis
* Region-wise Average Charges
* Dataset Overview Metrics

---

## 🚀 How to Run

### 1. Clone Repository

```bash
git clone https://github.com/bhupendra-ds27/insurance-cost-prediction.git
cd insurance-cost-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
streamlit run app.py
```

---

## ☁️ Live Deployment

### Streamlit Cloud

Live App:

(Add Your Streamlit Deployment Link Here)

---

## 🧠 Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Plotly
* Streamlit
* Pickle

### Machine Learning

* Linear Regression

### Deployment

* GitHub
* Streamlit Community Cloud

---

## 📈 Dashboard Visualizations

* Age vs Insurance Charges
* BMI vs Charges
* Smoker vs Non-Smoker Comparison
* Region-wise Average Insurance Charges
* Dataset Summary Metrics

---

## 🎯 Future Improvements

* Random Forest Regressor
* XGBoost Regressor
* SHAP Explainability
* Prediction History Tracking
* PDF Report Generation
* Docker Deployment
* FastAPI Backend Integration

---

## 👨‍💻 Author

**Bhupendra Chouhan**

B.Tech CSE (Data Science)
Oriental Institute of Science & Technology (OIST), Bhopal

GitHub: https://github.com/bhupendra-ds27

---

⭐ If you found this project useful, consider giving it a star on GitHub.
