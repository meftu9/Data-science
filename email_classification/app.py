import streamlit as st
import joblib

# ----------------------------
# Load model and vectorizer
# ----------------------------
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

# ----------------------------
# Title
# ----------------------------
st.title("📧 Spam Email Classification")
st.write("Detect whether an email or SMS message is **Spam** or **Ham (Not Spam)**.")

st.markdown("---")

# ----------------------------
# User Input
# ----------------------------
message = st.text_area(
    "Enter your Email or SMS Message",
    height=200,
    placeholder="Type your message here..."
)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:

        # Transform text
        message_vector = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(message_vector)[0]
        probability = model.predict_proba(message_vector)[0]

        if prediction == 1:
            confidence = probability[1]

            st.error("🚨 SPAM MESSAGE")
            st.write(f"**Confidence:** {confidence:.2%}")

        else:
            confidence = probability[0]

            st.success("✅ HAM (NOT SPAM)")
            st.write(f"**Confidence:** {confidence:.2%}")

        st.markdown("---")

        st.subheader("Prediction Probabilities")

        st.write(f"**Ham:** {probability[0]:.2%}")
        st.progress(float(probability[0]))

        st.write(f"**Spam:** {probability[1]:.2%}")
        st.progress(float(probability[1]))