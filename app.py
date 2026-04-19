import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Student Exam Score Predictor")

with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        study_hours = st.number_input("Study Hours", 0.0, 12.0)
        sleep_hours = st.number_input("Sleep Hours", 0.0, 12.0)
        attendance = st.slider("Attendance", 0, 100)

        internet_usage = st.number_input("Internet Usage", 0.0, 12.0)
        exercise_hours = st.number_input("Exercise Hours", 0.0, 5.0)

    with col2:
        mobile_usage = st.number_input("Mobile Usage", 0.0, 12.0)
        diet_quality = st.slider("Diet Quality", 1, 5)
        stress_level = st.slider("Stress Level", 1, 10)

        mental_health = st.slider("Mental Health", 1, 10)
        social_activity = st.slider("Social Activity", 1, 10)

    with col3:
        previous_score = st.number_input("Previous Score", 0, 100)
        class_participation = st.slider("Class Participation", 1, 5)
        assignment_completion = st.slider("Assignment Completion", 0, 100)

        parental_support = st.slider("Parental Support", 1, 5)
        extracurricular = st.slider("Extracurricular", 1, 5)

    submit = st.form_submit_button("Predict Score")

if submit:
    data = np.array([[study_hours, sleep_hours, attendance, mobile_usage,
                      internet_usage, exercise_hours, diet_quality, stress_level,
                      mental_health, social_activity, previous_score,
                      class_participation, assignment_completion,
                      parental_support, extracurricular]])

    data = scaler.transform(data)
    result = model.predict(data)[0]

    st.success(f"Predicted Score: {result:.2f}")
