import streamlit as st

def show_analysis_page(movie_names, movie_ratings, movie_genres):
    st.title('Detailed Analysis of Recommended Movies')

    st.write("### Movie Ratings Distribution")
    st.bar_chart(movie_ratings)

    st.write("### Top Genres Among Recommended Movies")
    genre_counts = {}
    for genres in movie_genres:
        for genre in genres:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
    top_genres = dict(sorted_genres[:5])
    st.bar_chart(top_genres)

    st.write("### Top Rated Movies")
    for name, rating in zip(movie_names, movie_ratings):
        st.write(f"- {name}: {rating}")

    st.write("### Movie Descriptions")
    for name, description in zip(movie_names, movie_descriptions):
        st.write(f"**{name}:** {description}")

    st.write("### Movie Trailers")
    for name, trailer_url in zip(movie_names, movie_trailers):
        st.markdown(f"[Watch Trailer for {name}]({trailer_url})")
