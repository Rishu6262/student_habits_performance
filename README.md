# 🎓 Student Performance Prediction using Machine Learning

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Regressor-success)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

### 📊 Predict Student Exam Scores Using Machine Learning Regression

*An end-to-end Machine Learning project that predicts student academic performance based on lifestyle, study habits, and personal factors.*

</div>

---

## 🌐 Live Demo

🚀 **Try the Web Application Here**

**🔗 https://studenthabitsperformance-4h6uedfpnyfxlcvewhkk5q.streamlit.app/**

---

# 📌 Project Overview

The **Student Performance Prediction System** is an end-to-end **Machine Learning Regression** project developed using **Python**, **Scikit-Learn**, **XGBoost**, **Pandas**, **NumPy**, and **Streamlit**. The objective of this project is to predict a student's **exam score** by analyzing various academic, lifestyle, and personal factors.

The model evaluates multiple attributes such as **study hours, attendance, sleep duration, social media usage, Netflix usage, exercise frequency, diet quality, internet quality, parental education level, mental health rating, and extracurricular participation** to estimate student performance accurately.

This project demonstrates the complete **Machine Learning workflow**, including **data preprocessing, exploratory data analysis (EDA), feature engineering, model training, performance evaluation, model comparison, and deployment through an interactive Streamlit web application**. It provides valuable insights into the factors that influence academic success while showcasing practical applications of predictive analytics in education.

---

## Features
- Data loading and exploration
- Missing value handling
- Duplicate data checking
- Categorical data encoding
- Feature scaling
- Train-test split
- Multiple regression model training
- Performance comparison using R² score
- Model saving using Pickle
- Ready for deployment integration

---

## Dataset Information
The dataset contains **1000 student records** with **16 features** related to student habits and academic performance.

### Features Used
- student_id
- age
- gender
- study_hours_per_day
- social_media_hours
- netflix_hours
- part_time_job
- attendance_percentage
- sleep_hours
- diet_quality
- exercise_frequency
- parental_education_level
- internet_quality
- mental_health_rating
- extracurricular_participation
- exam_score (Target Variable)

### Dataset Summary
- Total rows: 1000
- Total columns: 16
- Missing values found in `parental_education_level`: 91
- Final dataset after cleaning: 909 rows

---

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Pickle

---

## Machine Learning Workflow

### 1. Data Collection
The dataset is loaded using Pandas.

### 2. Data Exploration
Performed:
- `head()`
- `tail()`
- `shape`
- `info()`
- `describe()`
- null value checking

### 3. Data Cleaning
- Removed missing values using `dropna()`
- Checked duplicate records
- Encoded categorical columns using LabelEncoder

Encoded columns:
- student_id
- gender
- part_time_job
- diet_quality
- parental_education_level
- extracurricular_participation
- internet_quality

### 4. Feature Selection
Target column:
- exam_score

Input features:
- All remaining columns

### 5. Data Splitting
Dataset split:
- Training data: 80%
- Testing data: 20%

### 6. Feature Scaling
StandardScaler used for scaling numerical features.

---

## Models Used
The following regression models were trained:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Decision Tree Regressor
- XGBoost Regressor

---

## Model Performance (R² Score)

| Model | R² Score |
|------|---------|
| Linear Regression | 0.8881 |
| Ridge Regression | 0.8881 |
| Lasso Regression | 0.8793 |
| Random Forest Regressor | 0.8784 |
| Decision Tree Regressor | 0.6536 |
| XGBoost Regressor | 0.8779 |

### Best Performing Model
**Ridge Regression** achieved the highest R² score.

---

## Model Saving
Saved files:
- `model.pkl`
- `scaler.pkl`

Used:
```python
pickle.dump(rf, open("model.pkl", "wb"))
pickle.dump(sc, open("scaler.pkl", "wb"))
