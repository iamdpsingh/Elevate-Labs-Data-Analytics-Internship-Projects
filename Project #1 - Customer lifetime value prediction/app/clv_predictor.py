import streamlit as st
import pandas as pd
import os
import joblib

# Get the directory this file is in
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the model using absolute path
model_path = os.path.join(CURRENT_DIR, "model.pkl")
model = joblib.load(model_path)

# App UI
st.title("💰 Customer Lifetime Value Predictor")
st.markdown("Enter the customer behavior data to predict CLV.")

# Input Fields
freq = st.number_input("Frequency (Number of Purchases)", min_value=1)
rec = st.number_input("Recency (Days since first purchase)", min_value=1)
mon = st.number_input("Monetary Value (Total Spend)", min_value=1.0)

if st.button("Predict CLV"):
    input_df = pd.DataFrame([[freq, rec, mon]], columns=["Frequency", "Recency", "Monetary"])
    pred = model.predict(input_df)[0]
    st.success(f"Predicted Customer Lifetime Value: ₹ {pred:,.2f}")

# to run file 
#streamlit run "f:/Data Analyst Internship Elevate Labs/Projects/Project #1 - Customer lifetime value prediction/app/clv_predictor.py"
