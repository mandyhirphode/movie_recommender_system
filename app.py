import streamlit as st
import pickle
import pandas as pd
import requests
import gdown  # Google Drive file fetch करण्यासाठी

# Google Drive URL (फाइल IDs वापरून)
movie_dict_url = 'https://drive.google.com/uc?id=1Vmsa2I_5_xgeh3crTrIoE6_tneLFZOZV'  # तुमचा movie_dict.pkl फाइल ID
similarity_url = 'https://drive.google.com/uc?id=1R91wgyf8ELWftBJaS-OlOfH-r2-nbpPP'  # तुमचा similarity.pkl फाइल ID

# Download pickle files from Google Drive
gdown.download(movie_dict_url, 'movie_dict.pkl', quiet=False)
gdown.download(similarity_url, 'similarity.pkl', quiet=False)

# Movies DataFrame आणि similarity matrix लोड करा
movies_dict = pickle.load(open("movie_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", 'rb'))

# Fetch movie poster from API
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Movie recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_lst = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_lst:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Streamlit app title
st.title("Movie Recommender System")

# Dropdown for selecting movie
selected_movie_name = st.selectbox(
     "Please choose the movie",
     movies['title'].values
)

# Recommend button
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
