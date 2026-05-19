# Student Performance Prediction using Machine Learning

## Project Overview
This project predicts student exam scores based on lifestyle, academic, and personal habit data using multiple machine learning regression algorithms. The main goal is to analyze how factors such as study hours, social media usage, sleep, attendance, exercise, and mental health impact academic performance.

The project includes data preprocessing, feature engineering, model training, model evaluation, and model serialization for future deployment.

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
