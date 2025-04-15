# 🎬 Movie Recommender System

This is a content-based movie recommender system that suggests similar movies based on a selected title.  
It uses movie metadata from TMDb and applies NLP techniques and cosine similarity for recommendations.

---

## 🚀 Features

- ✅ Content-based filtering using movie descriptions
- ✅ Cosine similarity for matching movie vectors
- ✅ Flask-based web application interface
- ✅ Responsive design (works on desktop/mobile)
- ✅ Pre-trained model (no training needed during runtime)

---

## 📁 Project Structure

Movie_Recommender/ │ 
├── app.py # Flask app 
├── movie_recommander_system.ipynb # Notebook used for model development 
├── requirements.txt # Python dependencies 
├── setup.sh / procfile # For deployment (Heroku, etc.) 
├── tmdb_5000_movies.csv # Dataset 
├── tmdb_5000_credits.csv # Dataset 
  └── static/ & templates/ # Flask frontend files (if present)

---

## 📦 Installation

1. **Clone this repository**

```
git clone https://github.com/mandyhirphode/movie_recommender_system.git
cd movie_recommender_system
Install dependencies
pip install -r requirements.txt'''

---

## 🧠 Model Files
This project depends on 3 pre-trained .pkl files.
Please download them and place them in the root directory:

movie_dict.pkl = 
movies.pkl = 
similarity.pkl =

---

## ▶️ Run the App

python app.py
Then open http://127.0.0.1:5000/ in your browser.

---

## 🌐 Demo
You can deploy this on Heroku, Render, or any cloud platform.

---

## 📊 Dataset Source
TMDb 5000 Movies and Credits Dataset from Kaggle

