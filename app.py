import streamlit as st
import numpy as np
import pickle
import os

# ---- LOAD MODEL SAFELY ----
if os.path.exists("model.pkl") and os.path.exists("scaler.pkl"):
    model = pickle.load(open("model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
else:
    st.error("Model or Scaler file not found!")
    st.stop()

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Student Score Predictor", layout="wide")

# ---- SIDEBAR ----
st.sidebar.title("🎯 Student Inputs")

study_hours = st.sidebar.slider("Study Hours", 0.0, 12.0, 4.0)
sleep_hours = st.sidebar.slider("Sleep Hours", 0.0, 12.0, 6.0)
attendance = st.sidebar.slider("Attendance (%)", 0, 100, 75)
mobile_usage = st.sidebar.slider("Mobile Usage (Hours)", 0.0, 12.0, 3.0)

predict_btn = st.sidebar.button("Predict Score")

# ---- MAIN TITLE ----
st.title("📊 Student Performance Dashboard")

# ---- LAYOUT ----
col1, col2 = st.columns(2)

# ---- INPUT DISPLAY ----
with col1:
    st.subheader("📌 Input Summary")
    st.write(f"Study Hours: {study_hours}")
    st.write(f"Sleep Hours: {sleep_hours}")
    st.write(f"Attendance: {attendance}%")
    st.write(f"Mobile Usage: {mobile_usage}")

# ---- PREDICTION ----
with col2:
    st.subheader("📈 Prediction Result")

    if predict_btn:
        try:
            input_data = np.array([[study_hours, sleep_hours, attendance, mobile_usage]])
            input_scaled = scaler.transform(input_data)

            prediction = model.predict(input_scaled)[0]

            st.metric(label="Predicted Score", value=f"{prediction:.2f}")

            # Performance Label
            if prediction > 80:
                st.success("Excellent Performance 🎉")
            elif prediction > 50:
                st.info("Average Performance 👍")
            else:
                st.error("Needs Improvement ⚠️")

        except Exception as e:
            st.error(f"Error: {e}")

# ---- FOOTER ----
st.markdown("---")
st.caption("Machine Learning based Student Score Prediction System")
