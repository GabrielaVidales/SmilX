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
# Menu status (default: compressed)
# ==============================
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open


# ==============================
# Dynamic variables
# ==============================
menu_open = st.session_state.menu_open
sidebar_width = 260 if menu_open else 72
content_margin_left = 24
toggle_icon = "❮❮" if menu_open else "❯❯"


# ==============================
# Sidebar HTML
# ==============================
if menu_open:
    sidebar_html = """
<div class='custom-sidebar'>
    <div class='custom-sidebar-inner'>
        <div class='sidebar-brand'>SmilX</div>
        <div class='sidebar-title'>Menu</div>
        <div class='sidebar-links'>
            <a href='/' target='_self'>Explore</a>
            <a href='#about' target='_self'>About</a>
            <a href='#team' target='_self'>Team</a>
            <a href='javascript:void(0)' onclick="var b=window.top.location.href.split('/')[0]+'//'+window.top.location.host; window.top.location.href=b+'/Publications';">Publications</a>
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
# CSS inside the page (for content styling)
# ==============================
st.markdown(f"""
<style>
/* =========================
   Ocultar UI nativa de Streamlit
   ========================= */
#MainMenu {{ visibility: hidden; }}
header {{ visibility: hidden; }}
footer {{ visibility: hidden; }}

/* =========================
   Fondo general
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
html, body {{
    overflow-x: hidden !important;
    max-width: 100vw !important;
}}
.stApp {{
    overflow-x: hidden !important;
    max-width: 100vw !important;
    width: 100vw !important;
}}

/* Ocultar sidebar nativo */
section[data-testid="stSidebar"] {{
    display: none !important;
}}

/* Desplazar contenido principal */
.stMain {{
    margin-left: {sidebar_width}px !important;
    width: calc(100vw - {sidebar_width}px) !important;
    max-width: calc(100vw - {sidebar_width}px) !important;
    overflow-x: hidden !important;
    transition: margin-left 0.25s ease, width 0.25s ease;
    box-sizing: border-box !important;
    padding-left: 0 !important;
}}

/* Contenedor interior */
.stApp > div[data-testid="block-container"],
div[data-testid="block-container"],
.stMainBlockContainer,
.main .block-container,
section.main > div {{
    width: 100% !important;
    max-width: 100% !important;
    padding-top: 84px !important;
    padding-left: {content_margin_left}px !important;
    padding-right: 24px !important;
    padding-bottom: 2rem !important;
    background: #030814 !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
}}

.stApp svg,
.stApp canvas,
.stApp .plot-container,
.stApp .element-container {{
    max-width: 100% !important;
}}

.stApp .element-container,
.stApp [data-testid="stVerticalBlock"] > div {{
    position: relative !important;
    z-index: 0 !important;
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
}}
.sidebar-title {{
    font-size: 15px;
    font-weight: 800;
    color: #ffffff;
    margin: 8px 8px 10px 8px;
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
   Botón toggle
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
   Contenido
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
    margin: 48px 0 12px 0;
    padding: 16px 20px;
    font-size: 16px;
    line-height: 1.7;
    text-align: justify;
    background: #0b1324;
    border: 1px solid #1b263c;
    border-radius: 16px;
    color: #f4f7fb;
    position: relative;
    z-index: 1;
    clear: both;
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

.stMain * {{
    max-width: 100% !important;
    box-sizing: border-box !important;
}}
.stMain p,
.stMain span,
.stMain label,
.stMain div,
.stMain h1,
.stMain h2,
.stMain h3 {{
    word-break: break-word !important;
    overflow-wrap: break-word !important;
    white-space: normal !important;
}}
.stMain button,
.stMain input,
.stMain select,
.sidebar-links a {{
    white-space: nowrap !important;
}}

@media (max-width: 600px) {{
    .custom-sidebar {{ width: 48px !important; }}
    .stMain {{
        margin-left: 48px !important;
        max-width: calc(100vw - 48px) !important;
    }}
    .description-text {{ font-size: 14px; padding: 12px; }}
}}
</style>

<!-- ======== SIDEBAR (inside iframe, fixed to page) ======== -->
{sidebar_html}

<!-- ======== TOPBAR: injected into parent document via JS ======== -->
<script>
(function() {{
    var WIN = window.parent || window;
    var DOC = WIN.document;

    // Remove previous topbar if exists (on reruns)
    var old = DOC.getElementById('smilx-topbar');
    if (old) old.remove();
    var oldStyle = DOC.getElementById('smilx-topbar-style');
    if (oldStyle) oldStyle.remove();

    // Inject CSS into parent
    var style = DOC.createElement('style');
    style.id = 'smilx-topbar-style';
    style.textContent = `
        #smilx-topbar {{
            position: fixed;
            top: 0; left: 0; right: 0;
            height: 56px;
            background: #ffffff;
            border-bottom: 1px solid #e8e8e8;
            z-index: 2147483647;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            font-family: Arial, Helvetica, sans-serif;
        }}
        #smilx-topbar .tb-inner {{
            width: 100%;
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 0 14px;
            box-sizing: border-box;
        }}
        #smilx-topbar .tb-brand {{
            font-size: 20px;
            font-weight: 800;
            color: #111111;
            white-space: nowrap;
            text-decoration: none;
        }}
        #smilx-topbar .tb-links {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-left: 8px;
        }}
        #smilx-topbar .tb-links a {{
            text-decoration: none;
            color: #111111;
            font-size: 15px;
            font-weight: 700;
            padding: 8px 12px;
            border-radius: 8px;
            transition: background 0.2s ease;
            white-space: nowrap;
        }}
        #smilx-topbar .tb-links a:hover {{ background: #f1f1f1; }}
        #smilx-topbar .tb-links a.active {{
            background: #111111;
            color: #ffffff;
        }}
        #smilx-topbar .tb-github {{
            margin-left: auto;
        }}
        #smilx-topbar .tb-github a {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 46px; height: 46px;
            border-radius: 10px;
            text-decoration: none;
            transition: background 0.2s ease;
        }}
        #smilx-topbar .tb-github a:hover {{ background: #f1f1f1; }}
        #smilx-topbar .tb-github img {{
            width: 28px; height: 28px;
            display: block;
        }}
        @media (max-width: 600px) {{
            #smilx-topbar .tb-links a {{ display: none; }}
            #smilx-topbar .tb-brand {{ font-size: 16px; }}
        }}
    `;
    DOC.head.appendChild(style);

    // Inject topbar HTML into parent body
    var bar = DOC.createElement('div');
    bar.id = 'smilx-topbar';
    bar.innerHTML = `
        <div class="tb-inner">
            <span class="tb-brand">SmilX</span>
            <div class="tb-links">
                <a href="/" class="active">Explore</a>
                <a href="#about">About</a>
                <a href="#team">Team</a>
                <a href="javascript:void(0)" onclick="var b=location.href.split('/')[0]+'//'+location.host; location.href=b+'/Publications';">Publications</a>
            </div>
            <div class="tb-github">
                <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
                </a>
            </div>
        </div>
    `;
    DOC.body.insertBefore(bar, DOC.body.firstChild);
}})();
</script>
""", unsafe_allow_html=True)


# ==============================
# Toggle button
# ==============================
if st.button(toggle_icon, key="toggle_menu_btn"):
    toggle_menu()
    st.rerun()


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
