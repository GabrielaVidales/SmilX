# ==============================
# Imports
# ==============================
from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space

from rdkit import Chem  # noqa: F401
import streamlit as st
from textwrap import dedent


# ==============================
# Configuración de la página
# ==============================
st.set_page_config(
    page_title="SmilX",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==============================
# Estado del menú
# ==============================
if "menu_open" not in st.session_state:
    st.session_state.menu_open = True

def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open


# ==============================
# Variables dinámicas
# ==============================
menu_open = st.session_state.menu_open
sidebar_width = 260 if menu_open else 72
content_left = sidebar_width + 20
toggle_icon = "❮❮" if menu_open else "❯❯"
brand_sidebar = "SmilX" if menu_open else "S"


# ==============================
# CSS
# ==============================
st.markdown(dedent(f"""
<style>
/* ===== Ocultar UI nativa de Streamlit ===== */
#MainMenu {{
    visibility: hidden;
}}
header {{
    visibility: hidden;
}}
footer {{
    visibility: hidden;
}}

/* ===== Base ===== */
html, body, [class*="css"] {{
    font-family: Arial, Helvetica, sans-serif;
}}

.stApp {{
    background: #ffffff;
}}

/* MUY IMPORTANTE: no forzar width en img global */
.stApp > div[data-testid="block-container"] {{
    max-width: 100% !important;
    padding-top: 84px !important;
    padding-left: {content_left}px !important;
    padding-right: 1.25rem !important;
    padding-bottom: 2rem !important;
}}

.stApp svg,
.stApp canvas,
.stApp .plot-container,
.stApp .element-container {{
    max-width: 100% !important;
}}

/* ===== Topbar ===== */
.custom-topbar {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 56px;
    background: #ffffff;
    border-bottom: 1px solid #e9e9e9;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    z-index: 9999;
    display: flex;
    align-items: center;
}}

.custom-topbar-inner {{
    width: 100%;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 14px;
    box-sizing: border-box;
}}

.topbar-brand {{
    font-size: 20px;
    font-weight: 800;
    color: #111111;
    white-space: nowrap;
}}

.topbar-links {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-left: 8px;
}}

.topbar-links a {{
    text-decoration: none;
    color: #111111;
    font-size: 15px;
    font-weight: 700;
    padding: 8px 12px;
    border-radius: 8px;
    transition: background 0.2s ease;
    white-space: nowrap;
}}

.topbar-links a:hover {{
    background: #f2f2f2;
}}

.github-box {{
    margin-left: auto;
    display: flex;
    align-items: center;
}}

.github-box a {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 38px;
    height: 38px;
    border-radius: 10px;
    text-decoration: none;
    transition: background 0.2s ease, transform 0.2s ease;
}}

.github-box a:hover {{
    background: #f2f2f2;
    transform: scale(1.04);
}}

.github-box img {{
    width: 22px !important;
    height: 22px !important;
    display: block;
    object-fit: contain;
}}

/* ===== Sidebar ===== */
.custom-sidebar {{
    position: fixed;
    top: 56px;
    left: 0;
    bottom: 0;
    width: {sidebar_width}px;
    background: #fafafa;
    border-right: 1px solid #e8e8e8;
    z-index: 9998;
    overflow: hidden;
}}

.custom-sidebar-inner {{
    padding: 14px 10px;
    height: 100%;
    box-sizing: border-box;
}}

.sidebar-brand {{
    font-size: 18px;
    font-weight: 800;
    color: #111111;
    margin-bottom: 18px;
    white-space: nowrap;
}}

.sidebar-title {{
    font-size: 15px;
    font-weight: 800;
    color: #111111;
    margin: 8px 8px 10px 8px;
}}

.sidebar-card {{
    margin: 0 6px 14px 6px;
    padding: 12px 14px;
    background: #ffffff;
    border: 1px solid #e9e9e9;
    border-radius: 12px;
    color: #333333;
    font-size: 14px;
    line-height: 1.45;
}}

.sidebar-links {{
    display: flex;
    flex-direction: column;
    gap: 4px;
}}

.sidebar-links a {{
    text-decoration: none;
    color: #111111;
    font-size: 15px;
    font-weight: 700;
    padding: 12px 12px;
    margin: 0 6px;
    border-radius: 10px;
    transition: background 0.2s ease;
    white-space: nowrap;
}}

.sidebar-links a:hover {{
    background: #ececec;
}}

.sidebar-collapsed {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 14px;
    margin-top: 10px;
}}

.sidebar-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #c9c9c9;
}}

/* ===== Botón toggle ===== */
div[data-testid="stButton"] > button {{
    width: 100%;
    border-radius: 10px;
    border: 1px solid #dcdcdc;
    background: #ffffff;
    color: #111111;
    font-weight: 800;
    padding: 0.45rem 0.75rem;
}}

div[data-testid="stButton"] > button:hover {{
    background: #f3f3f3;
    border-color: #c9c9c9;
}}

/* ===== Contenido ===== */
.page-title {{
    font-size: 34px;
    font-weight: 800;
    color: #111111;
    margin: 0 0 8px 0;
}}

.page-subtitle {{
    font-size: 17px;
    color: #5a5a5a;
    margin-bottom: 24px;
}}

.description-text {{
    max-width: 980px;
    margin: 20px auto;
    padding: 16px 20px;
    font-size: 16px;
    line-height: 1.7;
    text-align: justify;
    background: #fafafa;
    border: 1px solid #e9e9e9;
    border-radius: 16px;
    color: #222222;
}}

.content-card {{
    max-width: 980px;
    margin: 20px auto;
    padding: 22px;
    background: #ffffff;
    border: 1px solid #e9e9e9;
    border-radius: 16px;
    color: #222222;
}}

.content-card h3 {{
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 24px;
}}

.content-card p {{
    margin: 0;
    font-size: 16px;
    line-height: 1.65;
}}

.footer-wrap {{
    max-width: 980px;
    margin: 0 auto;
}}

/* ===== Responsive ===== */
@media (max-width: 900px) {{
    .topbar-links {{
        overflow-x: auto;
    }}

    .topbar-links a {{
        font-size: 13px;
        padding: 7px 9px;
    }}

    .topbar-brand {{
        font-size: 17px;
    }}
}}
</style>
"""), unsafe_allow_html=True)


# ==============================
# Topbar
# ==============================
st.markdown(dedent("""
<div class="custom-topbar">
    <div class="custom-topbar-inner">
        <div class="topbar-brand">SmilX</div>

        <div class="topbar-links">
            <a href="/" target="_self">Home</a>
            <a href="#about" target="_self">About us</a>
            <a href="#program" target="_self">Program</a>
            <a href="#publications" target="_self">Publications</a>
        </div>

        <div class="github-box">
            <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            </a>
        </div>
    </div>
</div>
"""), unsafe_allow_html=True)


# ==============================
# Sidebar fijo
# ==============================
sidebar_placeholder = st.empty()

if menu_open:
    sidebar_html = dedent(f"""
    <div class="custom-sidebar">
        <div class="custom-sidebar-inner">
            <div class="sidebar-brand">{brand_sidebar}</div>
            <div class="sidebar-title">Menu</div>
            <div class="sidebar-card">
                Explore the different sections of SmilX.
            </div>
            <div class="sidebar-links">
                <a href="/" target="_self">Home</a>
                <a href="#about" target="_self">About us</a>
                <a href="#program" target="_self">Program</a>
                <a href="#publications" target="_self">Publications</a>
                <a href="https://github.com/LuisOrz/SmilX" target="_blank">GitHub</a>
            </div>
        </div>
    </div>
    """)
else:
    sidebar_html = dedent(f"""
    <div class="custom-sidebar">
        <div class="custom-sidebar-inner">
            <div class="sidebar-brand">{brand_sidebar}</div>
            <div class="sidebar-collapsed">
                <div class="sidebar-dot"></div>
                <div class="sidebar-dot"></div>
                <div class="sidebar-dot"></div>
            </div>
        </div>
    </div>
    """)

sidebar_placeholder.markdown(sidebar_html, unsafe_allow_html=True)


# ==============================
# Botón toggle del menú
# ==============================
toggle_col1, toggle_col2 = st.columns([1, 8])
with toggle_col1:
    if st.button(toggle_icon, key="toggle_menu_btn"):
        toggle_menu()
        st.rerun()


# ==============================
# Función principal
# ==============================
def main():
    st.markdown('<div class="page-title">SmilX</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">SMILES generation and chemical space exploration platform.</div>',
        unsafe_allow_html=True
    )

    a = initial_parameters()

    with st.spinner("Please wait..."):
        _ = chemical_space(a)

    st.markdown(dedent("""
    <div class="description-text" id="about">
    By integrating five syntactic constraints—including branch limitations,
    balanced parentheses, and aromaticity exclusion—TokenSMILES minimizes
    redundant enumerations for alkanes and ensures valence and octet rule
    compliance through semantic parsing.

    Implemented in SmilX, an open-source tool, TokenSMILES successfully
    generates SMILES for classical organic systems.
    </div>
    """), unsafe_allow_html=True)

    st.markdown(dedent("""
    <div class="content-card" id="program">
        <h3>Program</h3>
        <p>
            This section can contain the main workflow of the application,
            conversion utilities, chemical-space generation, and all the
            interactive tools you want to expose to the user.
        </p>
    </div>
    """), unsafe_allow_html=True)

    st.markdown(dedent("""
    <div class="content-card" id="publications">
        <h3>Publications</h3>
        <p>
            Add here your related papers, documentation, references, or
            external links associated with SmilX.
        </p>
    </div>
    """), unsafe_allow_html=True)

    st.divider()

    st.markdown(dedent("""
    <div class="footer-wrap">
        <b>Web Designers: Gabriela Yasmin Vidales Ayala & José Emmanuel Soberanis Cáceres</b>
    </div>
    """), unsafe_allow_html=True)


# ==============================
# Punto de entrada
# ==============================
if __name__ == "__main__":
    main()
