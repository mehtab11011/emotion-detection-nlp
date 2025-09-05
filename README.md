# Emotion Detection NLP App 🎭  

## 📌 Project Overview  
This project is an **Emotion Detection System** built using **Natural Language Processing (NLP)**.  
It uses **TF-IDF vectorization** and a **Multinomial Naive Bayes (MNB)** model, trained on a **Kaggle dataset**, to classify emotions from text input.  

The app is deployed using **Streamlit** and can detect the following emotions:  
- 😊 Joy  
- 😢 Sadness  
- ❤️ Love  
- 😡 Anger  
- 😨 Fear  
- 😲 Surprise  

---

## 🚀 Features  
- Real-time emotion detection from user input text.  
- Six-class emotion classification.  
- Simple web interface built with Streamlit.  
- Clean and modular code (easy to extend).  

---

## 🛠️ Tech Stack  
- **Python 3**  
- **Scikit-learn** (TF-IDF + Naive Bayes)  
- **Streamlit** (Web App)  
- **Joblib** (Model Saving/Loading)  
- **Regex** (Text Cleaning)  

---

## 📦 Installation & Setup  

## 1. Clone the Repository  
```bash
git clone https://github.com/your-username/emotion-detection-nlp.git
cd emotion-detection-nlp
## 2. reate Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
##3. Install Dependencies
pip install -r requirements.txt
## 4. Run the Streamlit App
streamlit run emotion_app.py

###
| Input Text                      | Predicted Emotion |
| ------------------------------- | ----------------- |
| "I am so happy today!"          | Joy               |
| "I feel scared about the exam." | Fear              |
| "I love my family."             | Love              |
| "This makes me angry."          | Anger             |
| "I am feeling very sad."        | Sadness           |
| "Wow, that’s amazing!"          | Surprise          |


📌 How It Works

Input text is cleaned (lowercased, punctuation removed).

Text is transformed using TF-IDF vectorizer.

Multinomial Naive Bayes model predicts the most likely emotion.

The result is displayed in the Streamlit interface.

📽️ Demo Video

👉 https://www.linkedin.com/posts/mehtab-khan-855a9b296_ai-nlp-machinelearning-activity-7369622127529955331-t9FR?utm_medium=ios_app&rcm=ACoAAEe1QAEBO3NzVu3Py2U_ra_I1WmJ25gBC3s&utm_source=social_share_send&utm_campaign=copy_link

📜 License

This project is open-source and free to use.



