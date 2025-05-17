# 🧠 Customer Lifetime Value (CLV) Prediction Model

This project predicts customer lifetime value using purchase data. It includes a machine learning model trained on real-world retail data and a Streamlit interface for interaction.

## 🚀 Features

- RFM (Recency, Frequency, Monetary) based model
- Random Forest regression
- Clean Streamlit dashboard for live predictions
- Industrial-grade project structure

## 📁 Project Structure



## 📦 Setup

```bash
# Clone & enter
git clone https://github.com/yourusername/clv-predictor.git
cd customer-lifetime-value-streamlit

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Train model
jupyter notebook notebooks/clv_modeling.ipynb

# Run app
cd app
streamlit run clv_predictor.py



---

## ✅ 7. To Run Everything:

```bash
cd customer-lifetime-value-streamlit

# Setup venv (recommended)
python -m venv venv
source venv/bin/activate       # or venv\Scripts\activate on Windows

# Install all libraries
pip install -r requirements.txt

# Run notebook
jupyter notebook notebooks/clv_modeling.ipynb   # Train and save model

# Launch app
cd app
streamlit run clv_predictor.py
