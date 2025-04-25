import streamlit as st

st.set_page_config(page_title="Netflix Dashboard", layout="wide", page_icon=":rocket:")

st.title("Streamlytics: Netflix Data Portfolio")
st.header("🎬 Netflix Movie Review App")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", ["About Me", "Review Movie", "Contact"])

if page == "About Me":
    import about_me
    about_me.tampilkan_about_me()
elif page == "Contact":
    import contact
    contact.tampilkan_contact()
elif page == "Review Movie":
    import review_movie
    review_movie.tampilkan_review_movie()