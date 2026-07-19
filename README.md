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

# 💡 Why This Project?

Student academic performance is influenced by various factors beyond classroom learning, such as study habits, attendance, sleep, social media usage, mental health, exercise, and family background. Identifying how these factors affect exam scores can help educators and students make informed decisions to improve academic outcomes.

This project was developed to:

* 🎯 Predict student exam scores using Machine Learning.
* 📊 Analyze the impact of academic, lifestyle, and personal factors on student performance.
* 🧹 Practice data preprocessing, feature engineering, and exploratory data analysis (EDA).
* 🤖 Compare multiple regression algorithms to identify the best-performing model.
* 🌐 Build an end-to-end Machine Learning application with Streamlit deployment.
* 💼 Develop a practical portfolio project demonstrating real-world Machine Learning skills.

---

# ⭐ Project Speciality

What makes this project unique:

* 🤖 **End-to-End Machine Learning Pipeline** from data preprocessing to deployment.
* 📈 **Multiple Regression Models** trained and compared for performance.
* 🏆 **Best Model Selection** based on R² Score for accurate predictions.
* 📊 **Comprehensive Data Analysis** with preprocessing and feature engineering.
* 🌐 **Interactive Streamlit Web Application** for real-time exam score prediction.
* 💾 **Model Serialization** using Pickle for easy deployment and reuse.
* 🎓 **Real-World Educational Use Case** that demonstrates practical applications of predictive analytics.
* 🚀 **Portfolio-Ready Project** showcasing Python, Machine Learning, Data Analysis, and deployment skills.

---

## ✨ Features

The **Student Performance Prediction System** offers a comprehensive end-to-end Machine Learning pipeline, covering every stage from data preprocessing to exam score prediction.

* 📂 Load and explore student performance datasets
* 🔍 Detect and handle missing values efficiently
* 🧹 Identify and remove duplicate records
* 🔄 Encode categorical features using **LabelEncoder**
* 📊 Perform Exploratory Data Analysis (EDA) to uncover data patterns
* ⚙️ Apply data preprocessing and feature engineering techniques
* 📈 Scale numerical features using **StandardScaler**
* ✂️ Split the dataset into training and testing sets (80:20)
* 🤖 Train and compare multiple Machine Learning regression models
* 📉 Evaluate model performance using **R² Score**
* 🏆 Select the best-performing regression model based on accuracy
* 💾 Save the trained model and scaler using **Pickle** for future use
* 🌐 Predict student exam scores through an interactive **Streamlit Web Application**
* 🚀 Deploy the application for real-time predictions and easy accessibility

---
## 📊 Dataset Information

The project uses the **Student Performance Prediction Dataset**, which contains **1,000 student records** and **16 features** representing students' academic, lifestyle, and personal habits. These attributes are used to predict the **exam score** through Machine Learning regression models.

| Property            | Value                                  |
| ------------------- | -------------------------------------- |
| **Dataset Name**    | Student Performance Prediction Dataset |
| **Total Records**   | 1,000                                  |
| **Total Features**  | 16                                     |
| **Problem Type**    | Regression                             |
| **Target Variable** | `exam_score`                           |

### 📋 Dataset Features

#### 👤 Student Information

* `student_id`
* `age`
* `gender`

#### 📚 Academic Habits

* `study_hours_per_day`
* `attendance_percentage`
* `extracurricular_participation`

#### 🌿 Lifestyle Factors

* `sleep_hours`
* `exercise_frequency`
* `diet_quality`
* `part_time_job`

#### 🌐 Digital & Entertainment Usage

* `social_media_hours`
* `netflix_hours`
* `internet_quality`

#### 🧠 Personal & Family Factors

* `mental_health_rating`
* `parental_education_level`

#### 🎯 Target Variable

* `exam_score` *(Student's Final Exam Score)*


### Dataset Summary
- Total rows: 1000
- Total columns: 16
- Missing values found in `parental_education_level`: 91
- Final dataset after cleaning: 909 rows

---
## 🛠️ Technologies Used

This project was developed using Python and several powerful libraries for data analysis, machine learning, visualization, and model deployment.

### 💻 Programming Language

* **Python**

### 📚 Libraries & Tools

* **NumPy** – Numerical computing and array operations
* **Pandas** – Data manipulation and preprocessing
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical data visualization
* **Scikit-learn** – Machine learning algorithms and model evaluation
* **XGBoost** – Gradient boosting regression model
* **Pickle** – Model serialization and storage

---

# ⚙️ Machine Learning Workflow

The project follows a complete end-to-end Machine Learning pipeline to predict student exam scores accurately.

### **Step 1: Data Collection**

The student performance dataset is imported into Python using **Pandas** for preprocessing and analysis.

---

### **Step 2: Data Exploration**

The dataset is explored to understand its structure, quality, and statistical properties before preprocessing.

**Operations Performed:**

* 📄 View the first records using `head()`
* 📄 View the last records using `tail()`
* 📏 Check dataset dimensions with `shape`
* ℹ️ Display dataset information using `info()`
* 📊 Generate descriptive statistics using `describe()`
* 🔍 Detect missing values using `isnull().sum()`
* 🧹 Check duplicate records
* 📋 Analyze data types and feature distributions


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
# 📌 Conclusion

The **Student Performance Prediction System** is an end-to-end Machine Learning project that predicts students' exam scores based on academic, lifestyle, and personal factors. By applying data preprocessing, exploratory data analysis (EDA), feature engineering, and multiple regression algorithms, the system provides reliable performance predictions and valuable insights into the factors influencing academic success.

This project demonstrates practical skills in **Python**, **Machine Learning**, **Data Analysis**, **Model Evaluation**, and **Streamlit deployment**, making it an excellent portfolio project for aspiring **Data Scientists**, **Machine Learning Engineers**, and **Python Developers**.

---

# 👨‍💻 Author

**Rishu Gurjar**

🎓 B.Tech Student | Aspiring Data Science 

### 📬 Connect with Me

* 💼 **LinkedIn:** https://www.linkedin.com/in/rishu-gurjar-7611042b2
* 💻 **GitHub:** https://github.com/Rishu6262

---
