# ==============================
# Imports
# ==============================
from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space

from rdkit import Chem  # noqa: F401
import streamlit as st


# ==============================
# Configuración de página
# ==============================
st.set_page_config(
    page_title="SmilX",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==============================
# Estado del menú (default: comprimido)
# ==============================
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open


# ==============================
# Variables dinámicas
# ==============================
menu_open = st.session_state.menu_open
sidebar_width = 260 if menu_open else 72
content_margin_left = 24  # padding interno fijo, el desplazamiento lo hace stMain
toggle_icon = "❮❮" if menu_open else "❯❯"


# ==============================
# HTML del sidebar (se construye antes del f-string para evitar SyntaxError)
# ==============================
if menu_open:
    sidebar_html = """
<div class='custom-sidebar'>
    <div class='custom-sidebar-inner'>
        <div class='sidebar-brand'>SmilX</div>
        <div class='sidebar-title'>Menu</div>
        <div class='sidebar-links'>
            <a href='/' target='_self'>Home</a>
            <a href='#about' target='_self'>About us</a>
            <a href='#program' target='_self'>Program</a>
            <a href='javascript:void(0)' onclick="window.parent.location.pathname='/publications';">Publications</a>
            <a href='https://github.com/LuisOrz/SmilX' target='_blank'>GitHub</a>
        </div>
    </div>
</div>"""
else:
    sidebar_html = """
<div class='custom-sidebar'>
    <div class='custom-sidebar-inner'>
        <div class='sidebar-collapsed'>
            <div class='sidebar-dot'></div>
            <div class='sidebar-dot'></div>
            <div class='sidebar-dot'></div>
        </div>
    </div>
</div>"""


# ==============================
# CSS + Topbar + Sidebar en UN SOLO bloque
# (Esto evita que Streamlit muestre el HTML como texto crudo)
# ==============================
st.markdown(f"""
<style>
/* =========================
   Ocultar UI nativa
   ========================= */
#MainMenu {{ visibility: hidden; }}
header {{ visibility: hidden; }}
footer {{ visibility: hidden; }}

/* =========================
   Fondo general NEGRO
   ========================= */
html, body, [class*="css"] {{
    font-family: Arial, Helvetica, sans-serif;
    background: #030814;
    color: white;
}}
body {{ background: #030814; }}
.stApp {{
    background: #030814 !important;
    color: white !important;
}}

/* Evitar desbordamiento horizontal */
html, body, .stApp {{
    overflow-x: hidden !important;
    max-width: 100vw !important;
}}

/* Ocultar sidebar nativo de Streamlit */
section[data-testid="stSidebar"] {{
    display: none !important;
}}

/* Contenedor principal — múltiples selectores para cubrir todas las versiones de Streamlit */
.stApp > div[data-testid="block-container"],
div[data-testid="block-container"],
.stMainBlockContainer,
.main .block-container,
section.main > div {{
    max-width: 100% !important;
    padding-top: 84px !important;
    padding-left: {content_margin_left}px !important;
    padding-right: 1.2rem !important;
    padding-bottom: 2rem !important;
    background: #030814 !important;
    transition: padding-left 0.25s ease;
    box-sizing: border-box !important;
}}

/* Desplazar el contenido principal exactamente el ancho del sidebar */
.stMain {{
    margin-left: {sidebar_width}px !important;
    transition: margin-left 0.25s ease;
    padding-left: 0 !important;
    overflow-x: hidden !important;
}}

.stApp svg,
.stApp canvas,
.stApp .plot-container,
.stApp .element-container {{
    max-width: 100% !important;
}}

/* =========================
   Barra superior blanca
   ========================= */
.topbar {{
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 56px;
    background: #ffffff;
    border-bottom: 1px solid #e8e8e8;
    z-index: 9999;
    display: flex;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}}
.topbar-inner {{
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
.topbar-links a:hover {{ background: #f1f1f1; }}
.topbar-links a.active {{
    background: #111111;
    color: #ffffff;
    border-radius: 8px;
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
    width: 46px; height: 46px;
    border-radius: 10px;
    text-decoration: none;
    transition: background 0.2s ease, transform 0.2s ease;
}}
.github-box a:hover {{ background: #f1f1f1; transform: scale(1.04); }}
.github-box img {{
    width: 32px !important;
    height: 32px !important;
    display: block;
    object-fit: contain;
}}

/* =========================
   Sidebar izquierdo oscuro
   ========================= */
.custom-sidebar {{
    position: fixed;
    top: 56px; left: 0; bottom: 0;
    width: {sidebar_width}px;
    background: #070d1b;
    border-right: 1px solid #1a2235;
    z-index: 9998;
    overflow: hidden;
    transition: width 0.25s ease;
}}
.custom-sidebar-inner {{
    padding: 14px 10px;
    height: 100%;
    box-sizing: border-box;
}}
.sidebar-brand {{
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 20px;
    white-space: nowrap;
    opacity: 0;
    transition: opacity 0.2s ease;
}}
.sidebar-open .sidebar-brand {{
    opacity: 1;
}}
.sidebar-title {{
    font-size: 15px;
    font-weight: 800;
    color: #ffffff;
    margin: 8px 8px 10px 8px;
}}
.sidebar-card {{
    margin: 0 6px 24px 6px;
    padding: 12px 14px;
    background: #111c30;
    border: 1px solid #1d2a44;
    border-radius: 12px;
    color: #d9e3f3;
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
    color: #ffffff;
    font-size: 15px;
    font-weight: 700;
    padding: 12px 12px;
    margin: 0 6px;
    border-radius: 10px;
    transition: background 0.2s ease;
    white-space: nowrap;
}}
.sidebar-links a:hover {{ background: #141f34; }}
.sidebar-collapsed {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin-top: 60px;
}}
.sidebar-dot {{
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #3b82f6;
}}

/* =========================
   Botón toggle nativo
   ========================= */
div[data-testid="stButton"] > button {{
    position: fixed;
    top: 68px; left: 12px;
    z-index: 10000;
    width: 48px; height: 38px;
    border-radius: 10px;
    border: 1px solid #27405d;
    background: #111c30;
    color: white;
    font-weight: 800;
    box-shadow: 0 2px 8px rgba(0,0,0,0.22);
}}
div[data-testid="stButton"] > button:hover {{
    background: #18263f;
    border-color: #33547b;
}}

/* =========================
   Títulos y contenido
   ========================= */
.page-title {{
    font-size: 34px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 8px 0;
}}
.page-subtitle {{
    font-size: 17px;
    color: #b9c4d6;
    margin-bottom: 24px;
}}
.description-text {{
    max-width: 100%;
    margin: 12px 0;
    padding: 16px 20px;
    font-size: 16px;
    line-height: 1.7;
    text-align: justify;
    background: #0b1324;
    border: 1px solid #1b263c;
    border-radius: 16px;
    color: #f4f7fb;
}}
.content-card {{
    max-width: 980px;
    margin: 12px 0;
    padding: 22px;
    background: #0b1324;
    border: 1px solid #1b263c;
    border-radius: 16px;
    color: #ffffff;
}}
.content-card h3 {{
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 24px;
    color: #ffffff;
}}
.content-card p {{
    margin: 0;
    font-size: 16px;
    line-height: 1.65;
    color: #d9e3f3;
}}
.footer-wrap {{
    max-width: 980px;
    margin: 0 auto;
    color: #ffffff;
}}
.stMarkdown, .stText, p, span, label, div {{ color: inherit; }}

/* =========================
   Responsive
   ========================= */
@media (max-width: 900px) {{
    .topbar-links {{ overflow-x: auto; }}
    .topbar-links a {{ font-size: 13px; padding: 7px 9px; }}
    .topbar-brand {{ font-size: 17px; }}
}}
</style>

<!-- ======== TOPBAR ======== -->
<div class="topbar">
    <div class="topbar-inner">
        <div class="topbar-brand">SmilX</div>
        <div class="topbar-links">
            <a href="/" target="_self" class="active">Home</a>
            <a href="#about" target="_self">About us</a>
            <a href="#program" target="_self">Program</a>
            <a href="javascript:void(0)" onclick="window.parent.location.pathname='/publications';">Publications</a>
        </div>
        <div class="github-box">
            <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            </a>
        </div>
    </div>
</div>

<!-- ======== SIDEBAR ======== -->
{sidebar_html}
""", unsafe_allow_html=True)


# ==============================
# Botón toggle
# ==============================
if st.button(toggle_icon, key="toggle_menu_btn"):
    toggle_menu()
    st.rerun()


# ==============================
# Función principal
# ==============================
def main():
    a = initial_parameters()

    with st.spinner("Please wait..."):
        _ = chemical_space(a)

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
