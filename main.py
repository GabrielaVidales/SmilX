from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem  # noqa: F401
import streamlit as st

# Config de página
st.set_page_config(
    page_title="SmilX",
    layout="wide"
)

# CSS global
st.markdown("""
<script defer src="https://cloud.umami.is/script.js" data-website-id="bae529d6-c60a-4e59-965e-701a9bdaeae9"></script>
<style>
/* ====== Layout ancho completo ====== */
.stApp > div[data-testid="block-container"]{
    max-width: 100% !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-top: 40px !important; /* menos espacio negro */
}

.stApp [data-testid="stVerticalBlock"],
.stApp [data-testid="stHorizontalBlock"],
.stApp [data-testid="column"],
.stApp [data-testid="stContainer"]{
    width: 100% !important;
    max-width: 100% !important;
    flex: 1 1 auto !important;
}

.stApp svg,
.stApp canvas,
.stApp img,
.stApp .plot-container,
.stApp .element-container,
.stApp .stMarkdown div{
    max-width: 100% !important;
    width: 100% !important;
}

.stApp{
    margin: 0 !important;
    padding: 0 !important;
}

/* ====== Navbar fijo ====== */
.navbar{
    background-color: white;
    overflow: hidden;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 50px; /* delgada */
    z-index: 1000;
    box-shadow: 0 8px 10px -1px rgba(0,0,0,0.1);
    display: flex;
    align-items: center;
    padding: 0 10px;
    margin: 0; /* quitado margen negativo */
    border-bottom: 1px solid #f0f0f0;
}

.navbar-container{
    display: flex;
    gap: 12px;
    align-items: center;
    width: 100%;
    margin: 0;
    padding: 0;
}

.navbar a{
    color: black;
    padding: 8px 12px;
    text-decoration: none;
    font-size: 15px;
    font-weight: 700;
    transition: all .3s ease;
    border-radius: 8px;
    white-space: nowrap;
    display: flex;
    align-items: center;
}

.navbar a:hover{
    background-color: #f0f0f0;
}

.navbar a.active{
    background-color: #f0f0f0;
}

/* ====== GitHub a la derecha y pequeño ====== */
.github-icon{
    margin-left: auto;           /* empuja a la derecha */
    display: flex;
    align-items: center;
    padding: 0;
}

.github-icon a{
    display: inline-flex;
    align-items: center;
    padding: 6px;                /* clic cómodo sin verse grande */
    border-radius: 8px;
}

.github-icon img{
    height: 20px;                /* tamaño */
    width: 20px;                 /* <- faltaba ; */
    transition: transform .3s ease;
    display: block;
}

.github-icon img:hover{
    transform: scale(1.1);
}

/* ====== Grid moléculas ====== */
.molecule-grid, .isomer-grid, .cards-grid{
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)) !important;
    gap: 1rem !important;
    width: 100% !important;
}

.molecule-card, .isomer-card, .card{
    width: 100% !important;
}

/* ====== Texto descriptivo ====== */
.description-text {
    max-width: 900px;
    margin: 40px auto 20px auto; /* espacio extra arriba */
    padding: 12px;
    font-size: 16px;
    line-height: 1.6;
    text-align: justify;
    word-wrap: break-word;
    clear: both;  /* << evita traslape con grids flotantes */
    display: block;
}

/* Ocultar menús de Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.footer{ margin-top: 0 !important; }
</style>
""", unsafe_allow_html=True)

# HTML Navbar
st.markdown("""
<nav class="navbar">
    <div class="navbar-container">
        <a href="/" target="_self">Home</a>
        <a href="#about" target="_self">About us</a>
        <a href="#program" target="_self">Program</a>
        <a href="#publications" target="_self">Publications</a>
        <div class="github-icon">
            <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            </a>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

def main():
    a = initial_parameters()

    with st.spinner("Please wait..."):
        _ = chemical_space(a)

    with st.container():
        st.markdown("""
        <div class="description-text">
        By integrating five syntactic constraints—including branch limitations, balanced parentheses, and aromaticity exclusion—TokenSMILES minimizes redundant enumerations for alkanes and ensures valence and octet rule compliance through semantic parsing. Implemented in SmilX, an open-source tool, TokenSMILES successfully generates SMILES for classical organic systems.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    footer = st.container()
    with footer:
        st.divider()
        st.markdown(
            "**Web Designers: Gabriela Yasmin Vidales Ayala & José Emmanuel Soberanis Cáceres**",
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
