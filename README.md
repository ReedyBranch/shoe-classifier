# 👟 Shoe Review Classifier

This is an interactive NLP-powered web app that classifies Amazon UK shoe reviews into one of four categories: **Sneaker**, **Boot**, **Heel**, or **Sandal** — based solely on the written review text.

Built using Python, Scikit-learn, and Streamlit, this project demonstrates end-to-end machine learning deployment: from preprocessing and model training to live user interaction on the web.

---

## 🚀 Live Demo

👉 [Try the app here](https://shoe-classifier-mlseccdztpvhmqnrr9mtvf.streamlit.app)  

---

## 📌 Features

- ✅ Cleaned and preprocessed real-world product reviews using NLTK
- ✅ Vectorized text with TF-IDF
- ✅ Trained and evaluated multiple models (Logistic Regression, Random Forest)
- ✅ Visualized performance with confusion matrices and classification reports
- ✅ Deployed as a live app using Streamlit Cloud
- ✅ Accepts live user input and returns instant predictions

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, Scikit-learn, NLTK**
- **Streamlit** for web interface
- **Joblib** for model persistence

---

## 🧠 How It Works

1. The app loads a pre-trained logistic regression model and vectorizer.
2. When a user types a review, it is cleaned using standard NLP techniques (stopwords removal, lemmatization).
3. The cleaned review is transformed into TF-IDF features.
4. The model predicts the type of shoe based on the review content.

---

## 📂 Project Structure

shoe-classifier/
├── app.py # Streamlit app
├── requirements.txt # Dependencies
├── model/
│ ├── logreg_model.pkl # Trained ML model
│ └── vectorizer.pkl # TF-IDF vectorizer
├── notebook.ipynb # Model training & evaluation
└── README.md # This file

---

## 📈 Example Use

**Review**:  
> "Love how lightweight and comfortable they are — perfect for running!"

**Prediction**:  
> 🧠 Sneaker

---

## 🙋‍♂️ Author

**Reed Burchard**  
📬 [LinkedIn](https://www.linkedin.com/in/reed-burchard/)  

---

## 🧪 Future Improvements

- Add more shoe categories (e.g. flats, wedges, loafers)
- Use deep learning (LSTM or DistilBERT) for improved performance
- Let users upload reviews in bulk via CSV

---