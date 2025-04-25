import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def tampilkan_review_movie():
    st.title("🎥 Netflix Film Review & Actor Predictions")

    try:
        df = pd.read_csv("netflix_data.csv")
    except FileNotFoundError:
        st.error("File 'netflix_data.csv' tidak ditemukan.")
        return

    df.dropna(subset=['title'], inplace=True)
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year

    selected_type = st.sidebar.selectbox("Pilih Tipe Konten", options=["All"] + df['type'].dropna().unique().tolist())
    selected_genre = st.sidebar.text_input("Cari Genre", "")

    filtered_df = df.copy()
    if selected_type != "All":
        filtered_df = filtered_df[filtered_df['type'] == selected_type]
    if selected_genre:
        filtered_df = filtered_df[filtered_df['listed_in'].str.contains(selected_genre, case=False, na=False)]

    st.subheader("📊 Most Popular Genre Statistics")
    top_genres = filtered_df['listed_in'].str.split(', ', expand=True).stack().value_counts().head(10)
    fig, ax = plt.subplots()
    top_genres.plot(kind='barh', ax=ax, color='tomato')
    st.pyplot(fig)

    st.subheader("📈 Number of Films/Shows by Release Year")
    fig2, ax2 = plt.subplots()
    filtered_df['release_year'].value_counts().sort_index().plot(kind='line', ax=ax2, marker='o')
    st.pyplot(fig2)

    st.subheader("🎞️ Movie Review Example")
    sample = filtered_df.sample(3, random_state=42)
    for _, row in sample.iterrows():
        st.markdown(f"### {row['title']} ({row['release_year']})")
        st.markdown(f"**Genre:** {row['listed_in']} | **Country:** {row.get('country', 'Tidak diketahui')}")
        st.markdown(f"**Review:** _This film presents an engaging story and is worth watching._")
        st.markdown("---")

    st.subheader("🎭 Predictions Actor (Dummy)")
    st.markdown("Actor Predictions Based on Genre (Simulation):")
    genre_to_actor = {
        'Drama': 'Leonardo DiCaprio',
        'Comedy': 'Jim Carrey',
        'Action': 'Tom Cruise',
        'Horror': 'Toni Collette',
        'Romance': 'Rachel McAdams',
        'Documentary': 'David Attenborough'
    }

    for genre, actor in genre_to_actor.items():
        st.markdown(f"- **{genre}** → 🎬 _{actor}_")