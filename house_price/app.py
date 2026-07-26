import streamlit as st
import pandas as pd
import joblib
import json

# Load Saved Files

model = joblib.load("models/house_price_model.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

with open("models/features.json", "r") as f:
    feature_cols = json.load(f)

# Load Dataset (to get ranges)
df = pd.read_csv("houses_improved.csv")

st.set_page_config(page_title="House Price Prediction", layout="wide")

st.title("🏠 House Price Prediction")
st.write("Enter the house details below.")

user_data = {}

# Dynamic Input Fields

for col in feature_cols:

    if col in label_encoders:
        options = list(label_encoders[col].classes_)

        value = st.selectbox(col, options)

        encoded = label_encoders[col].transform([value])[0]

        user_data[col] = encoded

    else:

        min_val = float(df[col].min())
        max_val = float(df[col].max())
        mean_val = float(df[col].mean())

        value = st.number_input(
            col,
            min_value=min_val,
            max_value=max_val,
            value=mean_val
        )

        user_data[col] = value

# Predict Button

if st.button("Predict Price"):

    input_df = pd.DataFrame([user_data])

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]

    st.success(f"Predicted House Price: ${prediction:,.2f}")