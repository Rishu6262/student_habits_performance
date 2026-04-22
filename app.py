import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Student Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Get the directory where the script is located
BASE_DIR = Path(__file__).parent

# Define file paths
MODEL_PATH = BASE_DIR / "model.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"
FEATURES_PATH = BASE_DIR / "features.pkl"

# ✅ Caching to load files only once
@st.cache_resource
def load_model_files():
    """Load and cache model, scaler, and features"""
    try:
        # Check if all files exist
        missing_files = []
        if not MODEL_PATH.exists():
            missing_files.append("model.pkl")
        if not SCALER_PATH.exists():
            missing_files.append("scaler.pkl")
        if not FEATURES_PATH.exists():
            missing_files.append("features.pkl")
        
        if missing_files:
            raise FileNotFoundError(f"Missing files: {', '.join(missing_files)}")
        
        # Load files with proper resource management
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        
        with open(SCALER_PATH, "rb") as f:
            scaler = pickle.load(f)
        
        with open(FEATURES_PATH, "rb") as f:
            features = pickle.load(f)
        
        return model, scaler, features
    
    except FileNotFoundError as e:
        st.error(f"❌ Error: {e}")
        st.info("Please ensure all pickle files (model.pkl, scaler.pkl, features.pkl) are in the same directory as app.py")
        st.stop()
    except Exception as e:
        st.error(f"❌ Unexpected error loading files: {e}")
        st.stop()

# Load the model files
model, scaler, features = load_model_files()

# ✅ Validate features
def validate_features(features):
    """Validate that features is a list of strings"""
    if not isinstance(features, list):
        raise ValueError("Features must be a list")
    if not all(isinstance(f, str) for f in features):
        raise ValueError("All features must be strings")
    return True

try:
    validate_features(features)
except ValueError as e:
    st.error(f"❌ Feature validation error: {e}")
    st.stop()

# Title and description
st.title("🎓 Student Exam Score Predictor")
st.write("---")
st.write("""
This application predicts student exam scores based on their study habits and performance metrics.
Fill in all the inputs below to get a personalized prediction.
""")

# ✅ Dynamic input with proper validation
st.subheader("📊 Enter Student Information")

input_data = {}
cols = st.columns(3)

try:
    for i, feature in enumerate(features):
        col_index = i % 3
        
        # Add input with label
        value = cols[col_index].number_input(
            label=feature,
            value=0.0,
            step=0.1,
            format="%.2f"
        )
        input_data[feature] = value
except Exception as e:
    st.error(f"❌ Error creating input fields: {e}")
    st.stop()

# Prediction section
st.write("---")

if st.button("🔮 Predict Score", use_container_width=True, type="primary"):
    try:
        # ✅ Validate input
        if not input_data:
            st.error("❌ Please fill in at least one input field")
            st.stop()
        
        # ✅ Create DataFrame with correct column order
        df = pd.DataFrame([input_data])
        
        # ✅ Ensure columns match the order used during training
        df = df[features]
        
        # ✅ Check for missing features
        missing_features = set(features) - set(df.columns)
        if missing_features:
            st.error(f"❌ Missing features: {missing_features}")
            st.stop()
        
        # ✅ Validate data types
        if not all(df.dtypes.apply(lambda x: x in ['float64', 'int64', 'float32', 'int32'])):
            st.error("❌ All inputs must be numeric values")
            st.stop()
        
        # ✅ Scale and predict
        df_scaled = scaler.transform(df)
        prediction = model.predict(df_scaled)[0]
        
        # Display prediction
        st.write("---")
        st.subheader("📈 Prediction Result")
        
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                label="Predicted Exam Score",
                value=f"{prediction:.2f}",
                delta=None
            )
        
        with col2:
            # Performance interpretation
            if prediction >= 80:
                st.success("✅ Excellent Performance 🎉")
                performance_level = "Excellent (80-100)"
            elif prediction >= 60:
                st.info("👍 Good Performance")
                performance_level = "Good (60-79)"
            elif prediction >= 40:
                st.warning("⚠️ Average Performance")
                performance_level = "Average (40-59)"
            else:
                st.error("⛔ Needs Improvement")
                performance_level = "Needs Improvement (<40)"
            
            st.metric(label="Performance Level", value=performance_level)
        
        # Additional insights
        st.write("---")
        st.subheader("💡 Insights")
        
        if prediction >= 80:
            st.success("🌟 Excellent work! Keep maintaining your study habits and performance will continue to excel.")
        elif prediction >= 60:
            st.info("📚 Good performance! Focus on consistent study and you can reach excellence.")
        elif prediction >= 40:
            st.warning("⏰ There's room for improvement. Increase study time and focus on weak areas.")
        else:
            st.error("🎯 Significant improvement needed. Consider working with a tutor or study group.")
        
        # Show input summary
        with st.expander("📋 View Input Summary"):
            summary_df = pd.DataFrame(list(input_data.items()), columns=["Feature", "Value"])
            st.dataframe(summary_df, use_container_width=True)
    
    except ValueError as e:
        st.error(f"❌ Validation Error: {e}")
    except Exception as e:
        st.error(f"❌ Prediction Error: {str(e)}")
        st.info("Please check your inputs and try again. If the problem persists, contact support.")

# Footer
st.write("---")
st.caption("💻 Student Habits Performance Predictor | Built with Streamlit")
