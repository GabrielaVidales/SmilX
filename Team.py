import streamlit as st

st.set_page_config(
    page_title="SmilX – Team",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# CSS + Topbar (active: Team)
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
.topbar-brand { font-size: 20px; font-weight: 800; color: #111111; white-space: nowrap; }
.topbar-links { display: flex; align-items: center; gap: 4px; margin-left: 12px; }
.topbar-links a {
    text-decoration: none;
    color: #111111;
    font-size: 15px;
    font-weight: 700;
    padding: 8px 12px;
    border-radius: 8px;
    transition: background 0.2s ease;
    white-space: nowrap;
    cursor: pointer;
}
.topbar-links a:hover { background: #f1f1f1; }
.topbar-links a.active { background: #111111; color: #ffffff; }
.github-box { margin-left: auto; display: flex; align-items: center; }
.github-box a {
    display: inline-flex; align-items: center; justify-content: center;
    width: 40px; height: 40px; border-radius: 8px;
    text-decoration: none; transition: background 0.2s ease;
}
.github-box a:hover { background: #f1f1f1; }
.github-box img { width: 26px; height: 26px; display: block; }

.page-title { font-size: 32px; font-weight: 800; color: #ffffff; margin: 36px 0 6px 0; }
.page-subtitle { font-size: 16px; color: #b9c4d6; margin-bottom: 32px; line-height: 1.6; }

.member-card {
    background: #0b1324;
    border: 1px solid #1b263c;
    border-radius: 16px;
    padding: 22px 20px 18px 20px;
    height: 100%;
    box-sizing: border-box;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.member-card:hover {
    border-color: #3b82f6;
    box-shadow: 0 4px 24px rgba(59,130,246,0.10);
}
.member-name { font-size: 17px; font-weight: 800; color: #ffffff; margin: 0 0 4px 0; }
.member-role {
    font-size: 13px; color: #3b82f6; font-weight: 700;
    margin: 0 0 10px 0; text-transform: uppercase; letter-spacing: 0.04em;
}
.member-desc { font-size: 14px; color: #b9c4d6; line-height: 1.6; margin: 0 0 16px 0; }
.member-links { display: flex; gap: 8px; flex-wrap: wrap; }
.member-links a {
    text-decoration: none; font-size: 13px; font-weight: 700;
    padding: 6px 14px; border-radius: 8px; border: 1px solid #1b263c;
    color: #d9e3f3; background: #111c30;
    transition: background 0.2s ease, border-color 0.2s ease;
}
.member-links a:hover { background: #1a2f52; border-color: #3b82f6; color: #ffffff; }

.footer-wrap { margin: 0 auto; color: #ffffff; }
.stMarkdown, .stText, p, span, label, div { color: inherit; }
</style>

<script>
function smilxNav(path) {
    var origin = (window.top || window).location.origin;
    (window.top || window).location.href = origin + path;
}
</script>

<div class="topbar-wrap">
  <div class="topbar">
    <div class="topbar-inner">
      <span class="topbar-brand">SmilX</span>
      <div class="topbar-links">
        <a href="javascript:void(0)" onclick="smilxNav('/')">Explore</a>
        <a href="javascript:void(0)" onclick="smilxNav('/About')">About</a>
        <a href="javascript:void(0)" onclick="smilxNav('/Team')" class="active">Team</a>
        <a href="javascript:void(0)" onclick="smilxNav('/Publications')">Publications</a>
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
# Team data
# ==============================
team = [
    {
        "name": "Luis Armando Gonzalez-Ortiz",
        "role": "Developer of SmilX / TokenSMILES",
        "desc": "Researcher focused on computational chemistry, cheminformatics, and grammar-based representations of chemical space.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
    {
        "name": "Lisset Noriega",
        "role": "Researcher",
        "desc": "Computational chemist working on astrochemistry and theoretical exploration of molecular isomers.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
    {
        "name": "Filiberto Ortiz-Chi",
        "role": "Researcher",
        "desc": "Researcher in theoretical chemistry and molecular structure prediction.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
    {
        "name": "Gabriela Vidales-Ayala",
        "role": "Web Designer",
        "desc": "Researcher in computational chemistry and molecular modeling.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
    {
        "name": "Emmanuel Soberanis-Cáceres",
        "role": "Web Designer",
        "desc": "Researcher focused on theoretical and computational chemistry.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
    {
        "name": "Miriam Pescador-Rojas",
        "role": "Researcher",
        "desc": "Researcher in computational chemistry and molecular modeling.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
    {
        "name": "Amilcar Meneses-Viveros",
        "role": "Researcher",
        "desc": "Researcher working on computational chemistry and molecular design.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
    {
        "name": "Alan Aspuru-Guzik",
        "role": "Professor",
        "desc": "Leading researcher in AI-driven chemistry, quantum chemistry, and molecular discovery.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
    {
        "name": "Gabriel Merino",
        "role": "Professor",
        "desc": "Professor of theoretical chemistry specializing in molecular structure and chemical bonding.",
        "scholar": "https://scholar.google.com/",
        "linkedin": "https://linkedin.com/",
    },
]

# ==============================
# Page body
# ==============================
st.markdown('<div class="page-title">Team</div>', unsafe_allow_html=True)
st.markdown("""
<div class="page-subtitle">
  The SmilX / TokenSMILES project is developed by researchers at
  <b>Centro de Investigación y Estudios Avanzados (CINVESTAV) Mérida</b>.
</div>
""", unsafe_allow_html=True)

for i in range(0, len(team), 3):
    cols = st.columns(3, gap="medium")
    for col, member in zip(cols, team[i:i+3]):
        with col:
            st.markdown(f"""
<div class="member-card">
  <div class="member-name">{member['name']}</div>
  <div class="member-role">{member['role']}</div>
  <div class="member-desc">{member['desc']}</div>
  <div class="member-links">
    <a href="{member['scholar']}" target="_blank">Google Scholar</a>
    <a href="{member['linkedin']}" target="_blank">LinkedIn</a>
  </div>
</div>
""", unsafe_allow_html=True)

st.divider()
st.markdown("""
<div class="footer-wrap">
  <b>Web Designers: Gabriela Yasmin Vidales Ayala &amp; José Emmanuel Soberanis Cáceres</b>
</div>
""", unsafe_allow_html=True)
