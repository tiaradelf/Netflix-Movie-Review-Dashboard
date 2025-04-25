import streamlit as st

def tampilkan_contact():
    st.title("Contact")
    st.write("Contact me through the following link:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/tiara-delfira/)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/tiaradelf)"
    )

    # Email
    st.write("📧 Email: delfiratiara7@gmail.com")