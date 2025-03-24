import streamlit as st

# Import CSS

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

remote_css("https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/styles.css")

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
            <h1>Staff technique<br> <span>La dream team</span></h1>
        </div>
    </div>
    <hr>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        .page-break { page-break-before: always; }
    </style>
""", unsafe_allow_html=True)


col3, col4 = st.columns(2)

with col3:
    st.markdown(
        "<h3 style='text-align: center; color: white;'>Kilian</h3>",
        unsafe_allow_html=True
    )

    subcol1, subcol2 = st.columns(2)

    with subcol1:
        st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/kiliancadiou/" target="_blank">
                <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/linkedin.png?raw=true" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    with subcol2:
            st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://github.com/KilianCadiou" target="_blank">
                <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/github.png?raw=true" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )

    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/avatar-kilian.png?raw=true" height="400">
    </a>
    """,
    unsafe_allow_html=True
    )


    
with col4:
    st.markdown(
        "<h3 style='text-align: center; color: white;'>Cédric</h3>",
        unsafe_allow_html=True
    )

    subcol1, subcol2 = st.columns(2)

    with subcol1:
        st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/c3dr1c/" target="_blank">
                <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/linkedin.png?raw=true" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
  
    with subcol2:
            st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://github.com/DriixData" target="_blank">
                <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/github.png?raw=true" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/avatar-cedric.png?raw=true" height="400">
    </a>
    """,
    unsafe_allow_html=True
    )

            
st.markdown("""---""")

col5, col6 = st.columns(2)

with col5:

    st.markdown(
        "<h3 style='text-align: center; color: white;'>Romain</h3>",
        unsafe_allow_html=True
    )
    
    subcol1, subcol2 = st.columns(2)
    
    with subcol1:
        st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/romain-foucault-01b11a15a/" target="_blank">
                <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/linkedin.png?raw=true" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    with subcol2:
            st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/romain-foucault-01b11a15a/" target="_blank">
                <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/github.png?raw=true" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/avatar-romain.png?raw=true" height="400">
    </a>
    """,
    unsafe_allow_html=True
    )


with col6:
    st.markdown(
        "<h3 style='text-align: center; color: white;'>Malo</h3>",
        unsafe_allow_html=True
    )

    subcol1, subcol2 = st.columns(2)
    
    with subcol1:
        st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/malo-le-pors-5373a8273/" target="_blank">
                <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/linkedin.png?raw=true" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    with subcol2:
            st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://github.com/MaloBang" target="_blank">
                <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/github.png?raw=true" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://github.com/MaloBang/The-Rockmmendation/blob/main/streamlit/img/avatar-malo.png?raw=true" height="400">
        </div>
        """,
        unsafe_allow_html=True
    )
