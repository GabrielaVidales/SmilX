from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem  # noqa: F401
import streamlit as st

# =========================
# Configuración de página
# =========================
st.set_page_config(
    page_title="SmilX",
    page_icon="🧪",
    layout="wide"
)

# =========================
# CSS mínimo necesario
# =========================
st.markdown("""
<style>
/* ===== Base general ===== */
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

.stApp {
    background-color: #000000;
    color: white;
}

/* Contenedor principal */
.stApp > div[data-testid="block-container"] {
    max-width: 100% !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-top: 90px !important;   /* espacio para navbar fija */
    padding-bottom: 2rem !important;
}

/* Ocultar elementos default */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ===== Navbar superior ===== */
.custom-navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 58px;
    background: #ffffff;
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    border-bottom: 1px solid #e9e9e9;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.06);
}

.custom-navbar-inner {
    width: 100%;
    max-width: 1400px;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 18px;
}

.nav-left {
    display: flex;
    align-items: center;
    gap: 10px;
}

.nav-logo-text {
    font-size: 1.05rem;
    font-weight: 800;
    color: #111827;
    margin-right: 8px;
    white-space: nowrap;
}

.nav-menu {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}

.nav-item {
    text-decoration: none;
    color: #111827;
    font-size: 0.95rem;
    font-weight: 600;
    padding: 8px 14px;
    border-radius: 999px;
    transition: all 0.25s ease;
    white-space: nowrap;
}

.nav-item:hover {
    background-color: #f3f4f6;
    color: #000000;
}

.nav-item.active {
    background-color: #e5e7eb;
    color: #000000;
}

.nav-right {
    margin-left: auto;
    display: flex;
    align-items: center;
}

.github-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 38px;
    height: 38px;
    border-radius: 10px;
    transition: all 0.25s ease;
    text-decoration: none;
}

.github-link:hover {
    background-color: #f3f4f6;
    transform: scale(1.05);
}

.github-link img {
    width: 21px;
    height: 21px;
    display: block;
}

/* ===== Hero / cabecera ===== */
.hero-wrap {
    text-align: center;
    margin-top: 1.5rem;
    margin-bottom: 1.2rem;
}

.hero-title {
    font-size: 4.8rem;
    font-weight: 800;
    color: white;
    letter-spacing: 0.08em;
    margin-bottom: 0.7rem;
    line-height: 1;
}

.hero-subtext {
    color: white;
    font-size: 1.15rem;
    line-height: 1.7;
    max-width: 1050px;
    margin: 0 auto;
}

/* ===== Zona donde corre chemical_space ===== */
.chemspace-wrap {
    margin-top: 1.5rem;
    margin-bottom: 2.2rem;
}

/* ===== Caja de descripción inferior ===== */
.description-section {
    clear: both;
    display: block;
    width: 100%;
    margin-top: 2.5rem;
    margin-bottom: 1rem;
}

.description-card {
    max-width: 1180px;
    margin: 0 auto;
    background: #111111;
    border: 1px solid #2a2a2a;
    color: #f3f4f6;
    border-radius: 20px;
    padding: 1.35rem 1.5rem;
    line-height: 1.8;
    font-size: 1.05rem;
    text-align: justify;
    box-shadow: 0 10px 24px rgba(0,0,0,0.22);
}

/* ===== Footer ===== */
.footer-text {
    text-align: center;
    color: #cbd5e1;
    font-size: 0.95rem;
    padding-top: 0.4rem;
    padding-bottom: 0.3rem;
}

/* ===== Ajustes widgets streamlit ===== */
.stTextInput > div > div > input {
    background-color: #1b1b1b;
    color: white;
    border: 1px solid #2f2f2f;
}

.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}

/* evita que elementos queden pegados */
.element-container {
    margin-bottom: 0.6rem;
}
</style>
""", unsafe_allow_html=True)


# =========================
# Navbar superior
# =========================
st.markdown("""
<div class="custom-navbar">
    <div class="custom-navbar-inner">
        <div class="nav-left">
            <div class="nav-logo-text">SMILX</div>
            <div class="nav-menu">
                <a class="nav-item active" href="/" target="_self">Home</a>
                <a class="nav-item" href="#about" target="_self">About us</a>
                <a class="nav-item" href="#program" target="_self">Program</a>
                <a class="nav-item" href="#publications" target="_self">Publications</a>
            </div>
        </div>

        <div class="nav-right">
            <a class="github-link" href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


def render_header():
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-title">SMILX</div>
        <div class="hero-subtext">
            "Grammar-Driven SMILES Standardization with TokenSMILES" by Luis Armando Gonzalez-Ortiz,
            Lisset Noriega, Filiberto Ortiz, Gabriela Vidales-Ayala, Emmanuel Soberanis,
            Amílcar Meneses, Alan Aspuru-Guzik, and Gabriel Merino.<br>
            Centro de Investigación y Estudios Avanzados (Cinvestav) Mérida<br>
            GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 Copyright (C) 2007 Free Software Foundation
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_description():
    st.markdown("""
    <div class="description-section">
        <div class="description-card">
            By integrating five syntactic constraints—including branch limitations, balanced parentheses,
            and aromaticity exclusion—TokenSMILES minimizes redundant enumerations for alkanes and ensures
            valence and octet rule compliance through semantic parsing. Implemented in SmilX, an open-source
            tool, TokenSMILES successfully generates SMILES for classical organic systems.
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.divider()
    st.markdown("""
    <div class="footer-text">
        Web Designers: Gabriela Yasmin Vidales Ayala & José Emmanuel Soberanis Cáceres
    </div>
    """, unsafe_allow_html=True)


def main():
    render_header()

    a = initial_parameters()

    st.markdown('<div class="chemspace-wrap">', unsafe_allow_html=True)
    with st.spinner("Please wait..."):
        _ = chemical_space(a)
    st.markdown('</div>', unsafe_allow_html=True)

    # descripción separada del grid
    render_description()

    render_footer()


if __name__ == "__main__":
    main()
