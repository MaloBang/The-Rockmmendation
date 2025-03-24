import streamlit as st

# Import CSS

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

remote_css("https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/styles.css")

st.html(
   " <ul>"
        "<li>Structure page App ⌛</li>"
        "<li>Créer logo du service ⌛</li>"
        "<li>Bakground App ✅</li>"
        "<li>Menu gauche + emoji ✅</li>"
        "<li>Vérifier les typos ✅</li>"
    "</ul>"
)