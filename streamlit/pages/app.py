import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
from sklearn.neighbors import NearestNeighbors
from bs4 import BeautifulSoup
import requests
import re
import unidecode
navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
url_base = 'https://www.imdb.com'
url_base_title = 'https://www.imdb.com/fr/title/'

# FONCTIONS

def clean_text(text):
    # Convertir le texte en minuscules
    text = text.lower()
    # Enlever les accents
    text = unidecode.unidecode(text)
    # Supprimer tous les caractères non alphanumériques
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = text.replace(' ','')
    return text


def info_films(id):

    lien_trailer = "Aucune bande-annonce disponible"
    lien_affiche = "Aucune affiche disponible"
    liste_acteurs = []
    dico_photos_final = {}

    url_base = 'https://www.imdb.com'
    url_base_title = 'https://www.imdb.com/fr/title/'
    url_finale_title = f'{url_base_title}{id}'

    if id == None:
        return 

    #TRAILER

    html_title = requests.get(url_finale_title, headers={'User-Agent': navigator})
    html_title2 = html_title.content
    soup_title = BeautifulSoup(html_title2, 'html.parser')

    for balise_parent in soup_title.find_all('div', class_='ipc-page-content-container ipc-page-content-container--center'):
        for element in balise_parent.find_all('a', class_='ipc-lockup-overlay ipc-focusable'):
            try:
                if 'video' in element['href']:
                    trailer = element['href']
                    lien_trailer = f'{url_base}{trailer}'
                break
            except:
                lien_trailer = "Unknown"

    #AFFICHE

    html_affiche = requests.get(url_finale_title, headers={'User-Agent': navigator})
    html_affiche2 = html_affiche.content
    soup_affiche = BeautifulSoup(html_affiche2, 'html.parser')
    affiche = ''

    for balise_parent in soup_affiche.find_all('div', class_='ipc-page-content-container ipc-page-content-container--center'):
        for element in balise_parent.find_all('img', class_='ipc-image'):
            affiche += f", {element['src']}"

    affiche = affiche.split(', ')

    if "" in affiche:
        affiche.remove("")

    lien_affiche = affiche[0]

    #ACTEURS

    html_acteurs = requests.get(url_finale_title, headers={'User-Agent': navigator})
    html_acteurs2 = html_acteurs.content
    soup_acteurs = BeautifulSoup(html_acteurs2, 'html.parser')
    liste_acteurs = []
    for balise_parent in soup_acteurs.find_all('div', class_='sc-cd7dc4b7-7 vCane'):
        for element in balise_parent.find_all('a', class_='sc-cd7dc4b7-1 kVdWAO'):
            liste_acteurs.append(element.get_text().strip())

    if len(liste_acteurs) > 4:
        liste_acteurs = liste_acteurs[:4]

    #PHOTOS ACTEURS

    html_acteurs = requests.get(url_finale_title, headers={'User-Agent': navigator})
    html_acteurs2 = html_acteurs.content
    soup_acteurs = BeautifulSoup(html_acteurs2, 'html.parser')
    dico_photos = {}
    dico_photos_final = {}

    for balise_parent in soup_acteurs.find_all('img', class_='ipc-image'):
        dico_photos.update({balise_parent['alt'] : balise_parent['src']})

    for element in dico_photos.keys():
        if element in liste_acteurs:
            dico_photos_final.update({element : dico_photos[element]})

    return lien_trailer, lien_affiche, liste_acteurs, dico_photos_final

# Import des données



# Import CSS

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

remote_css("https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/styles.css")

# --------------


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
            <h1>The Rock'mendation<br> <span>Bienvenu sur notre service de recommandation de films</span></h1>
        </div>
    </div>
    <hr>
""", unsafe_allow_html=True)

from streamlit_app import df_encoded

liste_des_critère = ['Période', 'Popularité', 'Note du film', 'Genres', 'Companie de production', 'Acteurs', 'Réalisateurs', 'Duree']

checkbox = st.checkbox("Afficher plus d'options")

correspondance = {
    "Période": "Date_x",
    "Companie de production": "production_companies_name",
    "Réalisateurs": "Realisateur",
    "Duree": "Duree_x",
    "Popularité": "popularity_x",
    "Note du film": "moyenne_vote_x"
}

if checkbox :
    st.write("Avez-vous des préférences dans les recommandations ? :")
    selection = st.multiselect("Séléctionnez vos  :", liste_des_critère)
    selection = [correspondance.get(crit, crit) for crit in selection]

    for col in df_encoded.columns:
        if any(crit in col for crit in selection):  # Vérifie si un critère correspond au nom d'une colonne
            if pd.api.types.is_numeric_dtype(df_encoded[col]):  # Vérifie que la colonne est numérique
                df_encoded[col] *= 2



# Sélectionner le film

choix_film = st.text_input("👇 Choisissez votre film")

if choix_film:
    choix_film_clean = clean_text(choix_film)

    # Filtrer le dataframe en fonction de la recherche
    filtered_df = df_encoded[df_encoded['Titre_pour_recherche'].str.contains(choix_film_clean, na=False)]

    # Si des résultats sont trouvés, afficher les films les plus populaires
    if not filtered_df.empty:
        filtered_df_sorted = filtered_df.sort_values(by='popularity_x', ascending=False).head(10)
        selected_film = st.selectbox("Sélectionnez votre film", filtered_df_sorted['Titre'])
    else:
        st.write("Aucun film trouvé. Vous pouvez élargir la recherche.")
        
        # Option pour afficher plus de films
    show_all = st.checkbox("Afficher tous les films correspondant à la recherche")
        
    if show_all:
        extended_df = filtered_df.sort_values(by='popularity_x', ascending=False).head(100)
        selected_film = st.selectbox("Sélectionnez votre film", extended_df['Titre'])


    if selected_film:
        st.markdown("---")
        titre_film = selected_film

        selected_film = df_encoded[df_encoded['Titre'] == titre_film]



    if not selected_film.empty:
        html_str = f"""
        <h2 class="titre_film">🎬{titre_film}</h2>
        <p class="caract_film">{int(selected_film['Date_y'])} - {str(list(selected_film['Genres'])).replace("[", "").replace("]", "").replace('"', '').replace("'", "").capitalize()}</p> 
        """
    st.markdown(html_str, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    lien_trailer, lien_affiche, liste_acteurs, dico_photos_final = info_films(selected_film['tconst'].iloc[0])

    with col1:
        st.image(lien_affiche, use_container_width=True)


    with col2:
        html_vote = f"<h3>⭐ Note : {round(float(selected_film['moyenne_vote_y']), 2)}/10</h3>"
        st.markdown(html_vote, unsafe_allow_html=True)
        st.markdown("---")
        html_description = f"<h4>{(selected_film['Description'].iloc[0])}</4>"
        st.markdown(html_description, unsafe_allow_html=True)
        st.markdown("---")
        html_trailer = f"<h4><a href={lien_trailer} target='_blank'>Trailer</a></4>"
        st.markdown(html_trailer, unsafe_allow_html=True)

    st.html("<h3>🤵 Casting</h3>")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        html_acteur1 = f"""<h3>{liste_acteurs[0]}</h3>"""
        st.markdown(html_acteur1, unsafe_allow_html=True)
        st.image(dico_photos_final[liste_acteurs[0]], use_container_width=True)

    with col2:
        html_acteur2 = f"""<h3>{liste_acteurs[1]}</h3>"""
        st.markdown(html_acteur2, unsafe_allow_html=True)
        st.image(dico_photos_final[liste_acteurs[1]], use_container_width=True)

    with col3:
        html_acteur3 = f"""<h3>{liste_acteurs[2]}</h3>"""
        st.markdown(html_acteur3, unsafe_allow_html=True)
        st.image(dico_photos_final[liste_acteurs[2]], use_container_width=True)

    with col4:
        html_acteur4 = f"""<h3>{liste_acteurs[3]}</h3>"""
        st.markdown(html_acteur4, unsafe_allow_html=True)
        st.image(dico_photos_final[liste_acteurs[3]], use_container_width=True)


    st.markdown("---")

    #######################
    #
    #         KNN
    #
    #######################

    # # CODE

    X = df_encoded

    k=13

    model = NearestNeighbors(n_neighbors=k, metric='euclidean')
    model.fit(X.drop(columns=['tconst', 'Titre', 'Titre_pour_recherche', 'Date_y', 'Duree_y', 'Genres', 'popularity_y', 'moyenne_vote_y', 'production_companies_name', 'Description', 'Realisateur', 'Acteurs']))

    distances, indices = model.kneighbors(selected_film.drop(columns=['tconst', 'Titre', 'Titre_pour_recherche', 'Date_y', 'Duree_y', 'Genres', 'popularity_y', 'moyenne_vote_y', 'production_companies_name', 'Description', 'Realisateur', 'Acteurs']))
    resultat = X.iloc[indices[0]].reset_index(drop=True)



    #######################
    #
    #       END  KNN
    #
    #######################


    st.html("<h2>🤙 Nos Rock'mendations</h2>")


    cols = st.columns(4)

    for i, col in enumerate(cols):
        lien_trailer, lien_affiche, liste_acteurs, dico_photos_final = info_films(resultat['tconst'].iloc[i+1])
        with col:
            st.image(lien_affiche, use_container_width=True)
            html_titre = f"<h5>{resultat['Titre'].iloc[i+1]}</4>"
            st.markdown(html_titre, unsafe_allow_html=True)
            html_note = f"<h5>⭐ Note : {round(resultat['moyenne_vote_y'].iloc[i+1], 2)}/10</4>"
            st.markdown(html_note, unsafe_allow_html=True)
            html_date = f"<h5>{int(resultat['Date_y'].iloc[i+1])}</4>"
            st.markdown(html_date, unsafe_allow_html=True)

    cols = st.columns(4)

    for i, col in enumerate(cols):
        lien_trailer, lien_affiche, liste_acteurs, dico_photos_final = info_films(resultat['tconst'].iloc[i+5])
        with col:
            st.image(lien_affiche, use_container_width=True)
            html_titre = f"<h5>{resultat['Titre'].iloc[i+5]}</4>"
            st.markdown(html_titre, unsafe_allow_html=True)
            html_note = f"<h5>⭐ Note : {round(resultat['moyenne_vote_y'].iloc[i+5], 2)}/10</4>"
            st.markdown(html_note, unsafe_allow_html=True)
            html_date = f"<h5>{int(resultat['Date_y'].iloc[i+5])}</4>"
            st.markdown(html_date, unsafe_allow_html=True)