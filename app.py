import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Student Predictor", layout="wide")

st.sidebar.title("Student Inputs")

study_hours = st.sidebar.slider("Study Hours", 0.0, 12.0, 4.0)
sleep_hours = st.sidebar.slider("Sleep Hours", 0.0, 12.0, 6.0)
attendance = st.sidebar.slider("Attendance (%)", 0, 100, 75)
mobile_usage = st.sidebar.slider("Mobile Usage", 0.0, 12.0, 3.0)
internet_usage = st.sidebar.slider("Internet Usage", 0.0, 12.0, 3.0)
exercise_hours = st.sidebar.slider("Exercise Hours", 0.0, 5.0, 1.0)

diet_quality = st.sidebar.slider("Diet Quality (1-5)", 1, 5, 3)
stress_level = st.sidebar.slider("Stress Level (1-10)", 1, 10, 5)
mental_health = st.sidebar.slider("Mental Health (1-10)", 1, 10, 6)
social_activity = st.sidebar.slider("Social Activity (1-10)", 1, 10, 5)

previous_score = st.sidebar.number_input("Previous Score", 0, 100, 60)
class_participation = st.sidebar.slider("Class Participation (1-5)", 1, 5, 3)
assignment_completion = st.sidebar.slider("Assignment Completion (%)", 0, 100, 70)
parental_support = st.sidebar.slider("Parental Support (1-5)", 1, 5, 3)
extracurricular = st.sidebar.slider("Extracurricular (1-5)", 1, 5, 3)

if st.sidebar.button("Predict"):
    data = np.array([[study_hours, sleep_hours, attendance, mobile_usage,
                      internet_usage, exercise_hours, diet_quality, stress_level,
                      mental_health, social_activity, previous_score,
                      class_participation, assignment_completion,
                      parental_support, extracurricular]])

    data = scaler.transform(data)
    result = model.predict(data)[0]

    st.title("Prediction Result")
    st.metric("Predicted Score", f"{result:.2f}")
