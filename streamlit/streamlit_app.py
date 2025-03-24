import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv(
        'https://github.com/MaloBang/The-Rockmmendation/raw/refs/heads/main/BD/X_encoded_film.csv.gz', 
        compression='gzip'
    )

df_encoded = load_data()
nav = get_nav_from_toml("streamlit\.streamlit\pages.toml")

# st.logo("logo.png")

pg = st.navigation(nav)

# add_page_title(pg)

# pg.run()


