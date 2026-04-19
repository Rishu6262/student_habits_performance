import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load files
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.set_page_config(page_title="Student Predictor", layout="wide")

st.title("🎓 Student Exam Score Predictor")

st.write("Fill all inputs to predict score")

# 🔥 Dynamic input (no mismatch ever)
input_data = {}

col1, col2, col3 = st.columns(3)

for i, feature in enumerate(features):
    if i % 3 == 0:
        input_data[feature] = col1.number_input(feature, value=0.0)
    elif i % 3 == 1:
        input_data[feature] = col2.number_input(feature, value=0.0)
    else:
        input_data[feature] = col3.number_input(feature, value=0.0)

# Prediction
if st.button("Predict Score"):
    try:
        df = pd.DataFrame([input_data])

        df_scaled = scaler.transform(df)
        prediction = model.predict(df_scaled)[0]

        st.success(f"Predicted Score: {prediction:.2f}")

        # Simple interpretation
        if prediction > 80:
            st.success("Excellent Performance 🎉")
        elif prediction > 50:
            st.info("Average Performance 👍")
        else:
            st.error("Needs Improvement ⚠️")

    except Exception as e:
        st.error(f"Error: {e}")
