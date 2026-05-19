Project Name: Student Performance Prediction using Machine Learning
The objective of this project was to predict student exam scores based on their academic habits, lifestyle, and personal factors such as study hours, attendance, sleep, social media usage, exercise, and mental health.

1. Dataset Collection

I used a student habits performance dataset containing 1000 student records and 16 features.

Some important features:

Study hours per day
Attendance percentage
Sleep hours
Social media usage
Netflix hours
Diet quality
Exercise frequency
Mental health rating
Exam score (target variable)
2. Exploratory Data Analysis (EDA)

To understand the dataset, I performed:

head()
tail()
shape
info()
describe()
missing value analysis

This helped me understand the data structure and quality.

3. Data Cleaning

I cleaned the dataset by:

checking missing values
finding null values in parental_education_level
removing missing records using dropna()
checking duplicate records

After cleaning, the dataset size became 909 records.

4. Data Preprocessing

Since machine learning models require numerical input, I converted categorical data into numeric format using Label Encoding.

Encoded columns:

gender
part_time_job
diet_quality
parental_education_level
internet_quality
extracurricular_participation
student_id
5. Feature Selection

I selected:
Target variable: exam_score

Input features: all remaining columns.

6. Train-Test Split

I divided the dataset into:

80% training data
20% testing data

using train_test_split() for model training and evaluation.

7. Feature Scaling

I applied StandardScaler to normalize feature values so that machine learning models could perform better.

8. Model Training

I trained multiple regression models to compare performance:

Linear Regression
Ridge Regression
Lasso Regression
Random Forest Regressor
Decision Tree Regressor
XGBoost Regressor
9. Model Evaluation

I evaluated all models using R² Score.

Results:

Linear Regression → 88.8%
Ridge Regression → 88.8%
Lasso Regression → 87.9%
Random Forest → 87.8%
XGBoost → 87.7%
Decision Tree → 65.3%

Best performing model:
Ridge Regression

10. Model Saving

Finally, I saved the trained model and scaler for future deployment using Pickle:

model.pkl
scaler.pkl
