import streamlit as st
import pandas as pd
import pickle

def recommend(movie):
    movies["title_L"] = movies["title"].apply(lambda x: x.lower())  # making a col. with all the lower case titles
    movie_index = movies[movies["title_L"] == movie.lower()].index[0]  # finding the index
    movies.drop("title_L", axis=1, inplace=True)  # removing that temprary lowecase list
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    movies_recommended = []
    for i in movie_list:
        movies_recommended.append(movies.iloc[i[0]].title)
        # print(movies.iloc[i[0]].title)
    return movies_recommended

movies = pd.read_pickle("model/movies_dict.pkl")
similarity = pd.read_pickle("model/similarity.pkl")
movies = pd.DataFrame(movies)

st.title("MOVIE RECOMMENDATION SYSTEM")

selected_movie = st.selectbox(
    "select a movie",
    movies["title"].values

)

if st.button("Recommend"):
    recommendations  = recommend(selected_movie)

    for i in recommendations:
        st.write(i)