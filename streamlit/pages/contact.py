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
                <img src="streamlit/img/linkedin.png" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    with subcol2:
            st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://github.com/KilianCadiou" target="_blank">
                <img src="streamlit/img/github.png" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )

    st.markdown(
    """
    <div style="text-align: center;">
        <img src="streamlit/img/avatar-kilian.png" height="400">
    </a>
    """,
    unsafe_allow_html=True
    )


    
with col4:
    st.markdown(
        "<h3 style='text-align: center; color: white;'>Loïc</h3>",
        unsafe_allow_html=True
    )

    subcol1, subcol2 = st.columns(2)

    with subcol1:
        st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/loic-fotsing-637a221a8/" target="_blank">
                <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/4096186-removebg-preview%20(1).png" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
        # st.image("/Users/kilian/Documents/GitHub/Test_projet_3/STREAMLIT/img/Sans titre.png", width = 50)
  
    with subcol2:
            st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://github.com/je-suis-lmfao" target="_blank">
                <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/Sans titre.png" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/377.png" height="400">
    </a>
    """,
    unsafe_allow_html=True
    )

            
st.markdown("""---""")

col5, col6 = st.columns(2)

with col5:

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
                <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/4096186-removebg-preview%20(1).png" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
        # st.image("/Users/kilian/Documents/GitHub/Test_projet_3/STREAMLIT/img/Sans titre.png", width = 50)
    with subcol2:
            st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://github.com/KilianCadiou" target="_blank">
                <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/Sans titre.png" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/POSE_-16.png" height="400">
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
                <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/4096186-removebg-preview%20(1).png" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    with subcol2:
            st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://github.com/MaloBang" target="_blank">
                <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/Sans titre.png" width="60">
            </a>
            """,
            unsafe_allow_html=True
            )
    
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/KilianCadiou/Va-Te-Faire-Foot/main/STREAMLIT/img/20092808-removebg-preview.png" height="400">
        </div>
        """,
        unsafe_allow_html=True
    )
