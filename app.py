import streamlit as st
import joblib
import os

MODEL_PATH = "spam_pipeline.joblib"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "Model file not found. Run train_model.py first."
        )
    return joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Spam Classification")
st.write(
    "Enter an email or SMS message to check whether "
    "it is spam or legitimate."
)

try:
    model = load_model()
except (FileNotFoundError, OSError, ValueError) as exc:
    st.error(f"Could not load the model: {exc}")
    st.stop()

message = st.text_area(
    "Enter your message",
    placeholder="Congratulations! You have won a free prize..."
)

if st.button("Classify Message", type="primary"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        prediction = int(model.predict([message])[0])

        if prediction == 1:
            st.error("🚨 This message is classified as SPAM.")
        else:
            st.success("✅ This message is classified as HAM.")

st.caption(
    "Predictions are model-based and may occasionally be incorrect."
)
