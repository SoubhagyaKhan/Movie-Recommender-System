import pandas as pd
import streamlit as st
import pickle
import requests
def fetch_poster(movie_id):
    resp=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=fc0afc2e21f4e81ba364b6299b286aea'.format(movie_id))
    data=resp.json()

    return 'https://image.tmdb.org/t/p/w185'+data['poster_path']



st.title('Movie Recommender System')
movies_dict=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movies=pd.DataFrame(movies_dict) 



def recommend(m):
    movie_index = movies[movies['title'] == m].index[0] 

    distance = similarity[movie_index]  

    mapping = list(enumerate(distance)) 

    movies_list = sorted(mapping, reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_poster

selected_movie_name =st.selectbox('Which Movie do you Like?',movies['title'].values)

if st.button('Recommend'):
    recommendations,posters=recommend(selected_movie_name)
    # for i in recommendations:
    #      st.write(i)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])