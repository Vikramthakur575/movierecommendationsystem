import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
# Function to fetch poster from TMDB
import streamlit as st
import requests

# Load API key from secrets.toml
tmdb_api_key = st.secrets["TMDB_API_KEY"]

def fetch_poster(movie_title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={movie_title}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data['results']:
            poster_path = data['results'][0].get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for {movie_title}: {e}")
    return "https://via.placeholder.com/200x300?text=No+Image"



# Recommend function
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"], []
    index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommended_titles = []
    recommended_posters = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_titles.append(title)
        recommended_posters.append(fetch_poster(title))
    return recommended_titles, recommended_posters


# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: #FF4500;'>🍿 Movie Recommender System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Select a movie below to get similar recommendations with posters!</p>",
    unsafe_allow_html=True
)

selected_movie = st.selectbox(
    '🎥 Select a movie:',
    movies['title'].values
)

if st.button('🔍 Recommend'):
    names, posters = recommend(selected_movie)

    st.markdown("## 🔗 Recommended Movies:")
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)

            st.markdown(f"<p style='text-align:center; color:#0066cc; font-weight:bold'>{names[i]}</p>",
                        unsafe_allow_html=True)


