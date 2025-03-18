import streamlit as st

# Import CSS

def local_css(styles):
    with open(styles) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("streamlit\styles.css")


st.markdown("""
    <style>
        .title-wrapper {
            display: flex;
            justify-content: center; /* Centre horizontalement */
            align-items: center; /* Centre verticalement si nécessaire */
            height: auto; /* Tu peux mettre 100vh pour centrer verticalement sur toute la page */
            text-align: center;
        }
        .title-container {
            background: rgba(0, 0, 0, 0.6);  /* Noir semi-transparent */
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        .title-container h1 {
            color: white;
            text-align: center;
            margin: 0;
        }
        .title-container span {
            color: #FFD700;  /* Jaune doré */
        }
    </style>
    <div class="title-wrapper">
        <div class="title-container">
            <h1>The Rock'mmendation <br> <span>Le projet</span></h1>
        </div>
    </div>
    <hr>
""", unsafe_allow_html=True)



st.html(
    "<p>Notre équipe de Data Analyst a été mandaté par un cinéma dans la Creuse qui se trouve en difficulté voulant passer le cap du digital.</p>"
)
st.markdown("""---""")
st.html(
    "<h2>🚀 Objectifs et enjeux :</h2>"
)

st.html(

    "<ol class='liste-objectifs'>"
        "<li>Réaliser une <a href='https://docs.google.com/document/d/1425NOxQd00ZuL6a4kvJx_Zy_HZoqKWVdUsUSLTS2GCw/edit?usp=sharing' target='_blank'>étude de marché</a> sur la consommation de cinéma dans la région.</li>"
        "<li>Mettre en avant certains <a href='KPI'>chiffres clés (KPI)</a> comme les acteurs les plus présents, l'âge moyen des acteurs...</li>"
        "<li>Créer une <a href='app'>Application</a> de recommandation de film en fonction des appréciations du spectateur.</li>"
    "</ol>"
)

st.markdown("""---""")

st.html(
    "<h2>⚙️ Stack technique : </h2>"
)

col1, col2, col3, col4 = st.columns(4)

with col1: 
    st.image("streamlit/img/Python.png")

with col2:
    st.image("streamlit/img/pandas_white.png")

with col3:
    st.image("streamlit/img/scikit-learn.png")

with col4:
    st.image("streamlit/img/Streamlit.png")

