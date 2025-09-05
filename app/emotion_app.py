import streamlit as st
import re
import joblib

# Load the model and vectorizer
model = joblib.load("emotion_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Emotion label mapping
emotion_map = {
    0: 'sadness',
    1: 'joy',
    2: 'love',
    3: 'anger',
    4: 'fear',
    5: 'surprise'
}

# Clean the input text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Predict emotion
def predict_emotion(text):
    cleaned = clean_text(text)
    vector = tfidf.transform([cleaned]).toarray()
    pred = model.predict(vector)[0]
    return emotion_map[pred]

# Streamlit UI
st.title("Emotion Detector 😄😢😡")
st.write("Type a message and detect its emotion!")

user_input = st.text_input("Enter your message:")

if user_input:
    result = predict_emotion(user_input)
    st.success(f"Predicted Emotion: **{result.upper()}**")
    
    
# streamlit run emotion_app.py
# >>


# https://www.kaggle.com/code/mehtabkhan001/notebookc0312e03e5/edit