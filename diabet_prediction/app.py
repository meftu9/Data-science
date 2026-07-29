import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("diabetes_model.pkl")

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction System")
st.write("Enter the patient's medical information below.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose", 0, 250, 120)
    blood_pressure = st.number_input("Blood Pressure", 0, 150, 70)
    skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)

with col2:
    insulin = st.number_input("Insulin", 0, 900, 80)
    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function",
        0.000,
        3.000,
        0.500,
        format="%.3f",
    )
    age = st.number_input("Age", 1, 120, 30)

st.markdown("---")

if st.button("Predict Diabetes", use_container_width=True):

    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        diabetes_pedigree,
        age
    ]])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ The patient is likely to have Diabetes.")
    else:
        st.success("✅ The patient is unlikely to have Diabetes.")

    # Show probability if supported
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0]

        st.markdown("### Confidence")

        st.write(f"Not Diabetic: {probability[0]:.2%}")
        st.progress(float(probability[0]))

        st.write(f"Diabetic: {probability[1]:.2%}")
        st.progress(float(probability[1]))