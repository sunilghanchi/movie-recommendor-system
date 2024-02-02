import streamlit as st
import requests
import pickle

background_image_path = 'D:\Linearloop Internship\Week-2\Day-4\image.jpg'

page_bg_img = f"""
<style>
body {{
    background-image: url("{background_image_path}");
    background-size: cover;
}}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(enumerate(similarity[index]), reverse=True, key= lambda x: x[1])
    recommended_movie = []
    recommend_movie_poster = []
    for i in distance[1:6]:
        recommended_movie.append(movies.iloc[i[0]].title)
        recommend_movie_poster.append(movies.iloc[i[0]].poster_path)
        
    return recommended_movie, recommend_movie_poster

st.header("Movie Recommendation System")

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select movie from dropdown list',
    movie_list)

st.write('Your selection is', selected_movie)

if st.button('Recommend the movies'):
    movies_name, movie_poster = recommend(selected_movie)
    
    cols_first_row = st.columns(3)
    for i in range(3):
        with cols_first_row[i]:
            st.text(movies_name[i])
            st.image(movie_poster[i], width=150)

    cols_second_row = st.columns(2)
    for i in range(3, 5):
        with cols_second_row[i - 3]: 
            st.text(movies_name[i])
            st.image(movie_poster[i], width=150)


