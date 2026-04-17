import streamlit as st
import numpy as np
import pickle

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Page config
st.set_page_config(page_title="Student Score Predictor", layout="centered")

# Title
st.title("Student Exam Score Predictor")
st.write("Enter student details to predict exam score")

# ---- INPUT SECTION ----
st.subheader("Input Features")

study_hours = st.number_input("Study Hours per Day", min_value=0.0, max_value=24.0, step=0.5)
sleep_hours = st.number_input("Sleep Hours per Day", min_value=0.0, max_value=24.0, step=0.5)
attendance = st.slider("Attendance (%)", 0, 100)
mobile_usage = st.number_input("Mobile Usage (Hours)", min_value=0.0, max_value=24.0, step=0.5)

# ---- PREDICTION ----
if st.button("Predict"):
    input_data = np.array([[study_hours, sleep_hours, attendance, mobile_usage]])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")

# ---- OPTIONAL INFO ----
st.markdown("---")
st.write("This model predicts exam performance based on student habits.")