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
# Estado del menú lateral
# ==============================
if "menu_expanded" not in st.session_state:
    st.session_state.menu_expanded = True


def toggle_menu():
    st.session_state.menu_expanded = not st.session_state.menu_expanded


# ==============================
# Parámetros dinámicos del layout
# ==============================
sidebar_width = 280 if st.session_state.menu_expanded else 70
main_margin_left = sidebar_width + 20
toggle_symbol = "❮❮" if st.session_state.menu_expanded else "❯❯"
logo_text = "SmilX" if st.session_state.menu_expanded else "S"


# ==============================
# CSS + HTML global
# ==============================
st.markdown(f"""
<script defer src="https://cloud.umami.is/script.js"
data-website-id="bae529d6-c60a-4e59-965e-701a9bdaeae9"></script>

<style>
/* =========================
   Reset básico
   ========================= */
html, body, [class*="css"] {{
    font-family: Arial, sans-serif;
}}

/* =========================
   Streamlit container
   ========================= */
.stApp > div[data-testid="block-container"] {{
    max-width: 100% !important;
    padding-top: 90px !important;
    padding-left: {main_margin_left}px !important;
    padding-right: 1rem !important;
    padding-bottom: 2rem !important;
}}

.stApp {{
    margin: 0 !important;
    padding: 0 !important;
}}

/* OJO: aquí ya NO incluimos .stApp img */
.stApp svg,
.stApp canvas,
.stApp .plot-container,
.stApp .element-container {{
    max-width: 100% !important;
}}

#MainMenu {{visibility: hidden;}}
header {{visibility: hidden;}}
footer {{visibility: hidden;}}

/* =========================
   Navbar superior
   ========================= */
.top-navbar {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 56px;
    background: #ffffff;
    border-bottom: 1px solid #e9e9e9;
    display: flex;
    align-items: center;
    z-index: 1001;
    box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    padding: 0 14px;
}}

.top-navbar-inner {{
    display: flex;
    align-items: center;
    width: 100%;
    gap: 12px;
}}

.brand {{
    font-size: 20px;
    font-weight: 800;
    color: #111111;
    white-space: nowrap;
    margin-right: 6px;
}}

.nav-links {{
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: nowrap;
}}

.nav-links a {{
    color: #111111;
    text-decoration: none;
    font-size: 15px;
    font-weight: 700;
    padding: 8px 12px;
    border-radius: 8px;
    transition: background 0.25s ease;
    white-space: nowrap;
}}

.nav-links a:hover {{
    background: #f1f1f1;
}}

.nav-links a.active {{
    background: #f1f1f1;
}}

.github-icon {{
    margin-left: auto;
    display: flex;
    align-items: center;
}}

.github-icon a {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px;
    border-radius: 10px;
    transition: background 0.25s ease, transform 0.2s ease;
}}

.github-icon a:hover {{
    background: #f1f1f1;
    transform: scale(1.04);
}}

.github-icon img {{
    width: 22px !important;
    height: 22px !important;
    display: block;
    object-fit: contain;
}}

/* =========================
   Sidebar izquierdo custom
   ========================= */
.left-sidebar {{
    position: fixed;
    top: 56px;
    left: 0;
    width: {sidebar_width}px;
    height: calc(100vh - 56px);
    background: #ffffff;
    border-right: 1px solid #ececec;
    z-index: 1000;
    transition: width 0.25s ease;
    overflow: hidden;
}}

.sidebar-inner {{
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: 14px 10px;
}}

.sidebar-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    margin-bottom: 18px;
}}

.sidebar-logo {{
    font-size: 20px;
    font-weight: 800;
    color: #111111;
    white-space: nowrap;
    overflow: hidden;
}}

.sidebar-toggle-space {{
    display: flex;
    justify-content: center;
    align-items: center;
}}

.sidebar-section-title {{
    font-size: 15px;
    font-weight: 800;
    color: #111111;
    margin: 12px 8px 10px 8px;
    white-space: nowrap;
}}

.sidebar-card {{
    background: #f7f7f7;
    border: 1px solid #ececec;
    border-radius: 12px;
    padding: 12px 14px;
    margin: 0 6px 14px 6px;
    color: #333333;
    font-size: 15px;
    line-height: 1.4;
}}

.sidebar-menu {{
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-top: 6px;
}}

.sidebar-menu a {{
    text-decoration: none;
    color: #111111;
    font-size: 16px;
    font-weight: 700;
    padding: 12px 12px;
    margin: 0 6px;
    border-radius: 10px;
    transition: background 0.2s ease;
    white-space: nowrap;
    overflow: hidden;
}}

.sidebar-menu a:hover {{
    background: #f2f2f2;
}}

.sidebar-collapsed-center {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    margin-top: 8px;
}}

.sidebar-mini-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #cfcfcf;
}}

/* =========================
   Botón Streamlit del toggle
   ========================= */
div.stButton > button {{
    width: 100%;
    border-radius: 10px;
    border: 1px solid #d9d9d9;
    background: white;
    color: #111111;
    font-weight: 700;
    padding: 0.45rem 0.75rem;
}}

div.stButton > button:hover {{
    border-color: #bfbfbf;
    background: #f5f5f5;
}}

/* =========================
   Texto descriptivo
   ========================= */
.description-text {{
    max-width: 980px;
    margin: 20px auto 24px auto;
    padding: 14px 18px;
    font-size: 16px;
    line-height: 1.7;
    text-align: justify;
    word-wrap: break-word;
    background: #fafafa;
    border: 1px solid #ececec;
    border-radius: 14px;
}}

.page-title {{
    font-size: 34px;
    font-weight: 800;
    color: #111111;
    margin-top: 8px;
    margin-bottom: 8px;
}}

.page-subtitle {{
    font-size: 17px;
    color: #555555;
    margin-bottom: 22px;
}}

.content-card {{
    border: 1px solid #ececec;
    border-radius: 16px;
    padding: 22px;
    background: white;
    margin-top: 18px;
}}

/* =========================
   Responsive
   ========================= */
@media (max-width: 900px) {{
    .nav-links {{
        gap: 4px;
        overflow-x: auto;
    }}

    .nav-links a {{
        font-size: 13px;
        padding: 7px 9px;
    }}

    .brand {{
        font-size: 17px;
    }}
}}
</style>
""", unsafe_allow_html=True)


# ==============================
# Navbar superior
# ==============================
st.markdown("""
<div class="top-navbar">
    <div class="top-navbar-inner">
        <div class="brand">SmilX</div>

        <div class="nav-links">
            <a href="/" target="_self">Home</a>
            <a href="#about" target="_self">About us</a>
            <a href="#program" target="_self">Program</a>
            <a href="#publications" target="_self">Publications</a>
        </div>

        <div class="github-icon">
            <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================
# Sidebar custom izquierdo
# ==============================
with st.container():
    sidebar_placeholder = st.empty()

with sidebar_placeholder.container():
    st.markdown(f"""
    <div class="left-sidebar">
        <div class="sidebar-inner">
            <div class="sidebar-header">
                <div class="sidebar-logo">{logo_text}</div>
                <div style="width: 56px;"></div>
            </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 4] if st.session_state.menu_expanded else [1, 1])

    with col1:
        if st.button(toggle_symbol, key="toggle_left_menu"):
            toggle_menu()
            st.rerun()

    if st.session_state.menu_expanded:
        st.markdown("""
            <div class="sidebar-section-title">Menu</div>

            <div class="sidebar-card">
                Explore the different sections of SmilX.
            </div>

            <div class="sidebar-menu">
                <a href="/" target="_self">Home</a>
                <a href="#about" target="_self">About us</a>
                <a href="#program" target="_self">Program</a>
                <a href="#publications" target="_self">Publications</a>
                <a href="https://github.com/LuisOrz/SmilX" target="_blank">GitHub</a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="sidebar-collapsed-center">
                <div class="sidebar-mini-dot"></div>
                <div class="sidebar-mini-dot"></div>
                <div class="sidebar-mini-dot"></div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)


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

    with st.container():
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

        st.markdown("""
        <div class="content-card" id="program">
            <h3 style="margin-top:0;">Program</h3>
            <p>
                This section can contain the main workflow of the application,
                conversion utilities, chemical-space generation, and all the
                interactive tools you want to expose to the user.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="content-card" id="publications">
            <h3 style="margin-top:0;">Publications</h3>
            <p>
                Add here your related papers, documentation, references, or
                external links associated with SmilX.
            </p>
        </div>
        """, unsafe_allow_html=True)

    footer = st.container()
    with footer:
        st.divider()
        st.markdown(
            "**Web Designers: Gabriela Yasmin Vidales Ayala & José Emmanuel Soberanis Cáceres**",
            unsafe_allow_html=True
        )


# ==============================
# Entry point
# ==============================
if __name__ == "__main__":
    main()
