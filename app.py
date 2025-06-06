import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load saved model and vectorizer
model = joblib.load("model/logreg_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# NLP preprocessing
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = re.sub(r"[^a-zA-Z]", " ", text.lower())
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)

# Streamlit UI
st.set_page_config(page_title="Shoe Review Classifier")
st.title("👟 Shoe Review Classifier")
st.markdown("Enter a review and we'll predict the shoe type (sneaker, boot, heel, or sandal).")

user_input = st.text_area("📝 Review Text", height=150)

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some review text.")
    else:
        cleaned = clean_text(user_input)
        vect_input = vectorizer.transform([cleaned])
        prediction = model.predict(vect_input)[0]
        st.success(f"🧠 Prediction: **{prediction.capitalize()}**")