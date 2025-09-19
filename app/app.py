import streamlit as st
import pickle
import re
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text) # remove punctuation/numbers
    text = text.lower()
    stop_words = set(stopwords.words("english"))
    text = " ".join([w for w in text.split() if w not in stop_words])
    return text

st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

st.title("📰 Fake News Detector")
st.write("Enter a news article and find out if it's **Fake** or **Real**.")

user_input = st.text_area("✍️ Paste news text here:")

if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]

        if prediction == 1:
            st.success("✅ **REAL news**.")
        else:
            st.error("❌ **FAKE news**.")