import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("Phishing_Email.csv", header=None)

df.columns = ['label', 'text']

X = df['text']
y = df['label']

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

st.title("Email Phishing Detector")

user_input = st.text_area("Paste Email Here")

if st.button("Check"):
    input_vec = vectorizer.transform([user_input])
    prediction = model.predict(input_vec)

    if prediction[0] == 1:
        st.error("⚠️ Phishing Email")
    else:
        st.success("✅ Legitimate Email")