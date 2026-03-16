# ==============================
# Imports
# ==============================
from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space_classic
from smilx_chemical_space import chemical_space_carbenes
from rdkit import Chem  # noqa: F401
import streamlit as st


# ==============================
# Website configuration
# ==============================
st.set_page_config(
    page_title="SmilX",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==============================
# CSS global + Topbar
# Strategy: the topbar is rendered as the very first element inside
# Streamlit's block-container. We use position:sticky + top:0 so it
# sticks to the top of the SCROLLABLE container (the page), which
# works reliably inside iframes unlike position:fixed.
# ==============================
st.markdown("""
<style>
/* =========================
   Ocultar UI nativa de Streamlit
   ========================= */
#MainMenu { visibility: hidden; }
header { visibility: hidden; }
footer { visibility: hidden; }

/* Ocultar sidebar nativo */
section[data-testid="stSidebar"] { display: none !important; }

/* =========================
   Fondo general
   ========================= */
html, body, [class*="css"] {
    font-family: Arial, Helvetica, sans-serif;
    background: #030814;
    color: white;
}
body { background: #030814; }
.stApp {
    background: #030814 !important;
    color: white !important;
    overflow-x: hidden !important;
}

/* Quitar padding-top que Streamlit agrega por defecto */
.stApp > div[data-testid="block-container"],
div[data-testid="block-container"],
.stMainBlockContainer,
.main .block-container {
    padding-top: 0 !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 100% !important;
    width: 100% !important;
}

/* =========================
   TOPBAR sticky
   ========================= */
.topbar-wrap {
    /* Negative margin compensa el padding del block-container
       para que la barra llegue al borde */
    margin: 0 -1rem 0 -1rem;
    position: sticky;
    top: 0;
    z-index: 9999;
}
.topbar {
    height: 56px;
    background: #ffffff;
    border-bottom: 1px solid #e8e8e8;
    display: flex;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
    width: 100%;
}
.topbar-inner {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 24px;
    box-sizing: border-box;
}
.topbar-brand {
    font-size: 20px;
    font-weight: 800;
    color: #111111;
    white-space: nowrap;
}
.topbar-links {
    display: flex;
    align-items: center;
    gap: 4px;
    margin-left: 12px;
}
.topbar-links a {
    text-decoration: none;
    color: #111111;
    font-size: 15px;
    font-weight: 700;
    padding: 8px 12px;
    border-radius: 8px;
    transition: background 0.2s ease;
    white-space: nowrap;
}
.topbar-links a:hover { background: #f1f1f1; }
.topbar-links a.active {
    background: #111111;
    color: #ffffff;
}
.github-box {
    margin-left: auto;
    display: flex;
    align-items: center;
}
.github-box a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px; height: 40px;
    border-radius: 8px;
    text-decoration: none;
    transition: background 0.2s ease;
}
.github-box a:hover { background: #f1f1f1; }
.github-box img {
    width: 26px;
    height: 26px;
    display: block;
}

/* =========================
   Contenido general
   ========================= */
.page-content {
    padding: 24px 0 2rem 0;
}
.description-text {
    max-width: 100%;
    margin: 48px 0 12px 0;
    padding: 16px 20px;
    font-size: 16px;
    line-height: 1.7;
    text-align: justify;
    background: #0b1324;
    border: 1px solid #1b263c;
    border-radius: 16px;
    color: #f4f7fb;
    clear: both;
}
.footer-wrap {
    margin: 0 auto;
    color: #ffffff;
}
.stMarkdown, .stText, p, span, label, div { color: inherit; }

@media (max-width: 600px) {
    .topbar-links a { font-size: 13px; padding: 6px 8px; }
    .topbar-brand { font-size: 17px; }
    .description-text { font-size: 14px; padding: 12px; }
}
</style>

<!-- ======== TOPBAR ======== -->
<div class="topbar-wrap">
    <div class="topbar">
        <div class="topbar-inner">
            <span class="topbar-brand">SmilX</span>
            <div class="topbar-links">
                <a href="/" target="_self" class="active">Explore</a>
                <a href="#about" target="_self">About</a>
                <a href="#team" target="_self">Team</a>
                <a href="javascript:void(0)" onclick="var b=window.top.location.href.split('/')[0]+'//'+window.top.location.host; window.top.location.href=b+'/Publications';">Publications</a>
            </div>
            <div class="github-box">
                <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
                </a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================
# Main function
# ==============================
def main():
    parameters = initial_parameters()

    if not(parameters.opt_carbenes) or parameters.molecular_formula['hdi'] == 0:
        with st.spinner("Please wait..."):
            _ = chemical_space_classic(parameters)
    else:
        with st.spinner("Please wait..."):
            _ = chemical_space_carbenes(parameters)

    # Spacer para separar el grid del texto inferior
    st.markdown("<div style='clear:both; margin-top: 48px;'></div>", unsafe_allow_html=True)

    st.markdown("""
<div class="description-text" id="about">
By integrating five syntactic constraints—including branch limitations,
balanced parentheses, and aromaticity exclusion—TokenSMILES minimizes
redundant enumerations for alkanes and ensures valence and octet rule
compliance through semantic parsing.

Implemented in SmilX, an open-source tool, TokenSMILES successfully
generates SMILES for classical organic systems.
</div>
""", unsafe_allow_html=True)

    st.divider()

    st.markdown("""
<div class="footer-wrap">
    <b>Web Designers: Gabriela Yasmin Vidales Ayala &amp; José Emmanuel Soberanis Cáceres</b>
</div>
""", unsafe_allow_html=True)


# ==============================
# Entry point
# ==============================
if __name__ == "__main__":
    main()
