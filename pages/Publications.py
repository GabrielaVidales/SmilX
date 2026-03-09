import streamlit as st

st.set_page_config(
    page_title="SmilX — Publications",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open

menu_open = st.session_state.menu_open
sidebar_width = 260 if menu_open else 72
content_margin_left = 24
toggle_icon = "❮❮" if menu_open else "❯❯"

if menu_open:
    sidebar_html = """
<div class='custom-sidebar'>
    <div class='custom-sidebar-inner'>
        <div class='sidebar-brand'>SmilX</div>
        <div class='sidebar-title'>Menu</div>
        <div class='sidebar-links'>
            <a href='/' target='_self'>Home</a>
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

publications = [
    {
        "authors": "Gonzalez-Ortiz, L. A.; Noriega, L.; Ortiz-Chi, F.; Vidales-Ayala, G.; Soberanis-Cáceres, E.; Meneses-Viveros, A.; Aspuru-Guzik, A.; Merino, G.",
        "title": "Grammar-Driven SMILES Standardization with TokenSMILES",
        "journal": "Chem. Sci.",
        "year": "2025",
        "doi": "10.1039/D5SC05004A",
        "url": "https://doi.org/10.1039/D5SC05004A",
    },
    {
        "authors": "Noriega, L.; Gonzalez-Ortiz, L. A.; Ortíz-Chi, F.; Ramírez, S. I.; Merino, G.",
        "title": "In Quest of the Missing C₂H₆O₂ Isomers in the Interstellar Medium: A Theoretical Search",
        "journal": "J. Phys. Chem. A",
        "year": "2024",
        "doi": "10.1021/acs.jpca.4c04102",
        "url": "https://doi.org/10.1021/acs.jpca.4c04102",
    },
    {
        "authors": "Noriega, L.; González-Ortiz, L. A.; Ortíz-Chi, F.; Quintal, A.; Ramírez, S. I.; Merino, G.",
        "title": "C₃H₈O₂ Isomers: Insights into Potential Interstellar Species",
        "journal": "J. Phys. Chem. A",
        "year": "2024",
        "doi": "10.1021/acs.jpca.4c04804",
        "url": "https://doi.org/10.1021/acs.jpca.4c04804",
    },
    {
        "authors": "Noriega, L.; Gonzalez-Ortiz, L. A.; Ortíz-Chi, F.; Merino, G.",
        "title": "Astrochemical Significance of C₂H₇NO Isomers: A Computational Perspective on Their Stability and Detectability",
        "journal": "J. Phys. Chem. A",
        "year": "2025",
        "doi": "10.1021/acs.jpca.5c01086",
        "url": "https://doi.org/10.1021/acs.jpca.5c01086",
    },
    {
        "authors": "Flores-Larrañaga, R.; Gonzalez-Ortiz, L. A.; Ortíz-Chi, F.; Castro, M. E.; Melendez, F. J.; Noriega, L.; Merino, G.",
        "title": "Computational Characterization of CH₄S₂ Isomers as Key Candidates in Interstellar Sulfur Chemistry",
        "journal": "ACS Earth Space Chem.",
        "year": "2025",
        "doi": "10.1021/acsearthspacechem.5c00223",
        "url": "https://doi.org/10.1021/acsearthspacechem.5c00223",
    },
]

pub_cards_html = ""
for i, p in enumerate(publications, 1):
    pub_cards_html += f"""
<div class="pub-card">
    <div class="pub-number">{i}</div>
    <div class="pub-body">
        <div class="pub-authors">{p['authors']}</div>
        <div class="pub-title">{p['title']}</div>
        <div class="pub-meta">
            <span class="pub-journal">{p['journal']}</span>
            <span class="pub-year">{p['year']}</span>
            <a class="pub-doi" href="{p['url']}" target="_blank" rel="noopener">DOI: {p['doi']}</a>
        </div>
    </div>
</div>"""

st.markdown(f"""
<style>
#MainMenu {{ visibility: hidden; }}
header {{ visibility: hidden; }}
footer {{ visibility: hidden; }}
html, body, [class*="css"] {{ font-family: Arial, Helvetica, sans-serif; background: #030814; color: white; }}
body {{ background: #030814; }}
html, body {{ overflow-x: hidden !important; max-width: 100vw !important; }}
.stApp {{ background: #030814 !important; color: white !important; overflow-x: hidden !important; max-width: 100vw !important; }}
section[data-testid="stSidebar"] {{ display: none !important; }}
.stMain {{ margin-left: {sidebar_width}px !important; width: calc(100vw - {sidebar_width}px) !important; max-width: calc(100vw - {sidebar_width}px) !important; overflow-x: hidden !important; transition: margin-left 0.25s ease, width 0.25s ease; box-sizing: border-box !important; padding-left: 0 !important; }}
.stApp > div[data-testid="block-container"], div[data-testid="block-container"], .stMainBlockContainer, .main .block-container, section.main > div {{ width: 100% !important; max-width: 100% !important; padding-top: 84px !important; padding-left: {content_margin_left}px !important; padding-right: 24px !important; padding-bottom: 2rem !important; background: #030814 !important; box-sizing: border-box !important; overflow-x: hidden !important; }}
.topbar {{ position: fixed; top: 0; left: 0; right: 0; height: 56px; background: #ffffff; border-bottom: 1px solid #e8e8e8; z-index: 9999; display: flex; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
.topbar-inner {{ width: 100%; display: flex; align-items: center; gap: 10px; padding: 0 14px; box-sizing: border-box; }}
.topbar-brand {{ font-size: 20px; font-weight: 800; color: #111111; white-space: nowrap; }}
.topbar-links {{ display: flex; align-items: center; gap: 8px; margin-left: 8px; }}
.topbar-links a {{ text-decoration: none; color: #111111; font-size: 15px; font-weight: 700; padding: 8px 12px; border-radius: 8px; transition: background 0.2s ease; white-space: nowrap; cursor: pointer; }}
.topbar-links a:hover {{ background: #f1f1f1; }}
.topbar-links a.active {{ background: #111111; color: #ffffff; }}
.github-box {{ margin-left: auto; display: flex; align-items: center; }}
.github-box a {{ display: inline-flex; align-items: center; justify-content: center; width: 46px; height: 46px; border-radius: 10px; text-decoration: none; transition: background 0.2s ease, transform 0.2s ease; }}
.github-box a:hover {{ background: #f1f1f1; transform: scale(1.04); }}
.github-box img {{ width: 32px !important; height: 32px !important; display: block; object-fit: contain; }}
.custom-sidebar {{ position: fixed; top: 56px; left: 0; bottom: 0; width: {sidebar_width}px; background: #070d1b; border-right: 1px solid #1a2235; z-index: 9998; overflow: hidden; transition: width 0.25s ease; }}
.custom-sidebar-inner {{ padding: 14px 10px; height: 100%; box-sizing: border-box; }}
.sidebar-brand {{ font-size: 18px; font-weight: 800; color: #ffffff; margin-bottom: 20px; white-space: nowrap; }}
.sidebar-title {{ font-size: 15px; font-weight: 800; color: #ffffff; margin: 8px 8px 10px 8px; }}
.sidebar-links {{ display: flex; flex-direction: column; gap: 4px; }}
.sidebar-links a {{ text-decoration: none; color: #ffffff; font-size: 15px; font-weight: 700; padding: 12px 12px; margin: 0 6px; border-radius: 10px; transition: background 0.2s ease; white-space: nowrap; cursor: pointer; }}
.sidebar-links a:hover {{ background: #141f34; }}
.sidebar-collapsed {{ display: flex; flex-direction: column; align-items: center; gap: 10px; margin-top: 60px; }}
.sidebar-dot {{ width: 8px; height: 8px; border-radius: 50%; background: #3b82f6; }}
div[data-testid="stButton"] > button {{ position: fixed; top: 68px; left: 12px; z-index: 10000; width: 48px; height: 38px; border-radius: 10px; border: 1px solid #27405d; background: #111c30; color: white; font-weight: 800; box-shadow: 0 2px 8px rgba(0,0,0,0.22); }}
div[data-testid="stButton"] > button:hover {{ background: #18263f; border-color: #33547b; }}
.page-title {{ font-size: 34px; font-weight: 800; color: #ffffff; margin: 0 0 4px 0; }}
.page-subtitle {{ font-size: 17px; color: #b9c4d6; margin-bottom: 28px; }}
.pub-card {{ display: flex; gap: 18px; align-items: flex-start; background: #0b1324; border: 1px solid #1b263c; border-radius: 14px; padding: 20px 22px; margin-bottom: 14px; width: 100%; box-sizing: border-box; transition: border-color 0.2s ease, box-shadow 0.2s ease; }}
.pub-card:hover {{ border-color: #2e4a72; box-shadow: 0 4px 18px rgba(46,74,114,0.18); }}
.pub-number {{ font-size: 22px; font-weight: 800; color: #3a6db5; min-width: 28px; padding-top: 2px; line-height: 1; }}
.pub-body {{ display: flex; flex-direction: column; gap: 5px; min-width: 0; }}
.pub-authors {{ font-size: 13px; color: #7a94b8; line-height: 1.4; word-break: break-word; }}
.pub-title {{ font-size: 16px; font-weight: 700; color: #e8eef7; line-height: 1.4; word-break: break-word; }}
.pub-meta {{ display: flex; flex-wrap: wrap; align-items: center; gap: 10px; margin-top: 2px; }}
.pub-journal {{ font-size: 13px; font-style: italic; color: #b9c4d6; }}
.pub-year {{ font-size: 13px; color: #b9c4d6; background: #111c30; border: 1px solid #1d2a44; border-radius: 6px; padding: 1px 8px; }}
.pub-doi {{ font-size: 12px; color: #4a90d9; text-decoration: none; border: 1px solid #1d3a5c; border-radius: 6px; padding: 2px 10px; transition: background 0.2s ease, color 0.2s ease; }}
.pub-doi:hover {{ background: #1a3a5c; color: #7ab8f5; }}
.stMarkdown, .stText, p, span, label, div {{ color: inherit; }}
</style>

<!-- TOPBAR -->
<div class="topbar">
    <div class="topbar-inner">
        <div class="topbar-brand">SmilX</div>
        <div class="topbar-links">
            <a href="/" target="_self">Home</a>
            <a href="javascript:void(0)" onclick="var b=window.top.location.href.split('/')[0]+'//'+window.top.location.host; window.top.location.href=b+'/Publications';" class="active">Publications</a>
        </div>
        <div class="github-box">
            <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            </a>
        </div>
    </div>
</div>

<!-- SIDEBAR -->
{sidebar_html}
""", unsafe_allow_html=True)

if st.button(toggle_icon, key="toggle_menu_btn"):
    toggle_menu()
    st.rerun()

st.markdown('<div class="page-title">Publications</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Research papers from the SmilX team.</div>', unsafe_allow_html=True)
st.markdown(pub_cards_html, unsafe_allow_html=True)
st.divider()
st.markdown('<div style="color:#ffffff;"><b>Web Designers: Gabriela Yasmin Vidales Ayala &amp; José Emmanuel Soberanis Cáceres</b></div>', unsafe_allow_html=True)
