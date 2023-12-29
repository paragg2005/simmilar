import requests
import streamlit as st
import pandas as pd
import pickle
import requests
st.header('Movie Recommender System',divider='red')

movies_list = pickle.load(open('moviesname.pkl','rb'))
movies = pd.DataFrame(movies_list)
similar = pickle.load(open('similar.pkl','rb'))
select = st.selectbox(label="",options= movies['title'].values)

def fetch_poster(movie_i):
    url = (f"https://api.themoviedb.org/3/movie/{movie_i}?language=en-US")

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5NTY4MGM4NTAyZWRiYTllMjIxMTY5ZmVkMGYyZjRhZiIsInN1YiI6IjY1N2RkZWQyZmQxNDBiMDc0YzgyNmE3OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P0a2xDfR6SAi029tYwLQll4VC0e9sF0hMmCTPbiYWj0"
    }

    response = requests.get(url, headers=headers,verify=False)


    poster = response.json()

    return "https://image.tmdb.org/t/p/w500"+poster['poster_path']



def recommend(movie):
    mov_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(enumerate(similar[mov_index]), reverse=True, key=lambda x: x[1])[1:7]
    recommend_movies=[]
    movies_poster=[]
    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,movies_poster
if st.button("Recommend"):
    names,posters = recommend(select)

    col1,col2,col3,col4,col5,col6=st.columns(6)
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
    with col6:
        st.text(names[5])
        st.image(posters[5])

genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy:smile:", "Drama:sunglasses:", "Documentary :movie_camera:","Action:fire:","Horror:skull:","Adventure:mountain:"])


