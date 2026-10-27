
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Email Phishing Detector", page_icon="🛡️")

st.title("🛡️ Email Phishing Detector")
st.write("Paste an email below to check whether it is safe or phishing.")

@st.cache_resource
def train_model():
    df = pd.read_csv("Phishing_Email.csv")

    # Handle the original dataset column names
    if "Email Type" in df.columns and "Email Text" in df.columns:
        df = df[["Email Type", "Email Text"]].copy()
        df.columns = ["label", "text"]
    elif "label" in df.columns and "text" in df.columns:
        df = df[["label", "text"]].copy()
    else:
        raise ValueError(
            f"Unexpected CSV columns: {df.columns.tolist()}"
        )

    df = df.dropna(subset=["text", "label"])
    df["text"] = df["text"].astype(str)
    df = df[df["text"].str.strip() != ""]

    X = df["text"]
    y = df["label"].astype(str).str.strip()

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_vec, y)

    return vectorizer, model

try:
    with st.spinner("Training the phishing detection model..."):
        vectorizer, model = train_model()

    user_input = st.text_area("Paste Email Here", height=180)

    if st.button("Check Email", type="primary"):
        if not user_input.strip():
            st.warning("Please paste an email first.")
        else:
            input_vec = vectorizer.transform([user_input])
            prediction = model.predict(input_vec)[0]
            label = str(prediction).strip().lower()

            if "phishing" in label:
                st.error("⚠️ This email is likely a Phishing Email.")
            else:
                st.success("✅ This email is likely a Safe Email.")

except Exception as e:
    st.error(f"Unable to load or train the model: {e}")
