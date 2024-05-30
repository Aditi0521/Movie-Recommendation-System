import streamlit as st
import pickle
import pandas as pd
from user_auth import register, login, logout
from utils import recommend
from database import create_db, fetch_history, save_recommendation

# Create the database if it doesn't exist
create_db()

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
simi = pickle.load(open('simi.pkl', 'rb'))

st.title('Movie Recommendation System')

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    # Navigation menu
    page = st.sidebar.radio("Navigation", ["Recommendations", "Recommendation History"])

    if st.sidebar.button("Logout"):
        logout()
        st.session_state.logged_in = False
        st.experimental_rerun()

    if page == "Recommendations":
        selected_movie_name = st.selectbox('Need recommendations for movies?', movies['title'].values)

        if st.button('Recommend'):
            names, posters, descriptions, ratings, genres_list, similarity_scores, trailers_list, actors_list, directors_list = recommend(
                selected_movie_name, movies, simi)
            for i in range(len(names)):
                with st.container():
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.image(posters[i])
                    with col2:
                        st.subheader(names[i])
                        st.text(f'Rating: {ratings[i]}')
                        st.text(f'Genres: {", ".join(genres_list[i])}')
                        st.text(f'Similarity Score: {similarity_scores[i]:.2f}%')
                        st.write(descriptions[i])
                        if trailers_list[i]:
                            st.markdown(f"[Watch Trailer]({trailers_list[i]})")
                        if actors_list[i]:
                            st.write('**Actors:**')
                            actor_row = st.columns(len(actors_list[i]))
                            for actor, actor_col in zip(actors_list[i], actor_row):
                                actor_col.info(actor)
                        if directors_list[i]:
                            st.write('**Directors:**')
                            director_row = st.columns(len(directors_list[i]))
                            for director, director_col in zip(directors_list[i], director_row):
                                director_col.success(director)
                        st.markdown('---')
                save_recommendation(st.session_state.user_id, movies.iloc[i].movie_id, names[i])

    elif page == "Recommendation History":
        st.subheader("Your Recommendation History")
        history = fetch_history(st.session_state.user_id)
        unique_movies = {}
        for record in history:
            if record[0] not in unique_movies:
                unique_movies[record[0]] = record[1]

        for movie, date in unique_movies.items():
            with st.expander(movie):
                st.write(f"Recommended on: {date}")
else:
    choice = st.sidebar.selectbox("Login/Register", ["Login", "Register"])
    if choice == "Login":
        login()
    else:
        register()
