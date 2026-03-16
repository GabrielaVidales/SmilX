import streamlit as st

st.set_page_config(
    page_title="SmilX – Publications",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# CSS + Topbar
# ==============================
st.markdown("""
<style>
#MainMenu { visibility: hidden; }
header { visibility: hidden; }
footer { visibility: hidden; }
section[data-testid="stSidebar"] { display: none !important; }

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

/* ── Topbar sticky ── */
.topbar-wrap {
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
.github-box { margin-left: auto; display: flex; align-items: center; }
.github-box a {
    display: inline-flex; align-items: center; justify-content: center;
    width: 40px; height: 40px; border-radius: 8px;
    text-decoration: none; transition: background 0.2s ease;
}
.github-box a:hover { background: #f1f1f1; }
.github-box img { width: 26px; height: 26px; display: block; }

/* ── Page content ── */
.page-content {
    padding: 36px 0 2rem 0;
}
.page-title {
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 32px 0;
}

/* ── Publication cards ── */
.pub-card {
    background: #0b1324;
    border: 1px solid #1b263c;
    border-radius: 16px;
    padding: 24px 26px;
    margin-bottom: 18px;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.pub-card:hover {
    border-color: #3b82f6;
    box-shadow: 0 4px 24px rgba(59,130,246,0.10);
}
.pub-title {
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 10px 0;
    line-height: 1.4;
}
.pub-authors {
    font-size: 14px;
    color: #b9c4d6;
    margin: 0 0 8px 0;
    line-height: 1.6;
}
.pub-journal {
    font-size: 14px;
    color: #7ea8d8;
    font-style: italic;
    margin: 0 0 6px 0;
}
.pub-doi {
    font-size: 13px;
    color: #4b6580;
    margin: 0 0 16px 0;
}
.pub-doi span { color: #5b8fbf; }
.pub-btn {
    display: inline-block;
    text-decoration: none;
    font-size: 13px;
    font-weight: 700;
    padding: 7px 18px;
    border-radius: 8px;
    border: 1px solid #1b263c;
    color: #d9e3f3;
    background: #111c30;
    transition: background 0.2s ease, border-color 0.2s ease;
}
.pub-btn:hover {
    background: #1a2f52;
    border-color: #3b82f6;
    color: #ffffff;
}

.footer-wrap { margin: 0 auto; color: #ffffff; }
.stMarkdown, .stText, p, span, label, div { color: inherit; }
</style>

<!-- ── TOPBAR ── -->
<div class="topbar-wrap">
  <div class="topbar">
    <div class="topbar-inner">
      <span class="topbar-brand">SmilX</span>
      <div class="topbar-links">
        <a href="/" target="_self">Explore</a>
        <a href="/About" target="_self">About</a>
        <a href="/Team" target="_self">Team</a>
        <a href="javascript:void(0)" onclick="var b=window.top.location.href.split('/')[0]+'//'+window.top.location.host; window.top.location.href=b+'/Publications';" class="active">Publications</a>
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
# Publications data
# ==============================
publications = [
    {
        "title": "Grammar-Driven SMILES Standardization with TokenSMILES",
        "authors": "Gonzalez-Ortiz, L. A.; Noriega, L.; Ortiz-Chi, F.; Vidales-Ayala, G.; Soberanis-Cáceres, E.; Meneses-Viveros, A.; Aspuru-Guzik, A.; Merino, G.",
        "journal": "Chem. Sci. 2025",
        "doi": "10.1039/D5SC05004A",
        "url": "https://doi.org/10.1039/D5SC05004A",
    },
    {
        "title": "In Quest of the Missing C2H6O2 Isomers in the Interstellar Medium: A Theoretical Search",
        "authors": "Noriega, L.; Gonzalez-Ortiz, L. A.; Ortíz-Chi, F.; Ramírez, S. I.; Merino, G.",
        "journal": "J. Phys. Chem. A 2024, 128 (32), 6757–6762.",
        "doi": "10.1021/acs.jpca.4c04102",
        "url": "https://doi.org/10.1021/acs.jpca.4c04102",
    },
    {
        "title": "C3H8O2 Isomers: Insights into Potential Interstellar Species",
        "authors": "Noriega, L.; González-Ortiz, L. A.; Ortíz-Chi, F.; Quintal, A.; Ramírez, S. I.; Merino, G.",
        "journal": "J. Phys. Chem. A 2024, 128 (46), 9964–9971.",
        "doi": "10.1021/acs.jpca.4c04804",
        "url": "https://doi.org/10.1021/acs.jpca.4c04804",
    },
    {
        "title": "Astrochemical Significance of C2H7NO Isomers: A Computational Perspective on Their Stability and Detectability",
        "authors": "Noriega, L.; Gonzalez-Ortiz, L. A.; Ortíz-Chi, F.; Merino, G.",
        "journal": "J. Phys. Chem. A 2025, 129 (21), 4715–4723.",
        "doi": "10.1021/acs.jpca.5c01086",
        "url": "https://doi.org/10.1021/acs.jpca.5c01086",
    },
    {
        "title": "Computational Characterization of CH4S2 Isomers as Key Candidates in Interstellar Sulfur Chemistry",
        "authors": "Flores-Larrañaga, R.; Gonzalez-Ortiz, L. A.; Ortíz-Chi, F.; Castro, M. E.; Melendez, F. J.; Noriega, L.; Merino, G.",
        "journal": "ACS Earth Space Chem. 2025",
        "doi": "10.1021/acsearthspacechem.5c00223",
        "url": "https://doi.org/10.1021/acsearthspacechem.5c00223",
    },
]


# ==============================
# Page body
# ==============================
st.markdown('<div class="page-content"><div class="page-title">Publications 📑</div></div>', unsafe_allow_html=True)

for pub in publications:
    st.markdown(f"""
<div class="pub-card">
  <div class="pub-title">{pub['title']}</div>
  <div class="pub-authors">{pub['authors']}</div>
  <div class="pub-journal">{pub['journal']}</div>
  <div class="pub-doi">DOI: <span>{pub['doi']}</span></div>
  <a class="pub-btn" href="{pub['url']}" target="_blank" rel="noopener">Open publication ↗</a>
</div>
""", unsafe_allow_html=True)

st.divider()
st.markdown("""
<div class="footer-wrap">
  <b>Web Designers: Gabriela Yasmin Vidales Ayala &amp; José Emmanuel Soberanis Cáceres</b>
</div>
""", unsafe_allow_html=True)
