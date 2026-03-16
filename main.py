# ==============================
# Imports
# ==============================
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
# Global CSS — styles Streamlit's native top nav
# to match the SmilX design system
# ==============================
st.markdown("""
<style>
/* ── Hide default Streamlit chrome ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
section[data-testid="stSidebar"] { display: none !important; }

/* ── Global background ── */
html, body, [class*="css"] {
    font-family: Arial, Helvetica, sans-serif;
    background: #030814;
    color: white;
}
body { background: #030814; }
.stApp {
    background: #030814 !important;
    color: white !important;
}

/* ── Style the native Streamlit top navigation bar ── */

/* Outer wrapper of the nav */
[data-testid="stHeader"],
header[data-testid="stHeader"] {
    visibility: visible !important;
    background: #ffffff !important;
    border-bottom: 1px solid #e8e8e8 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10) !important;
    height: 56px !important;
    display: flex !important;
    align-items: center !important;
}

/* Nav tabs container */
[data-testid="stHeaderNavItems"],
div[data-testid="stTopNavItems"] {
    display: flex !important;
    align-items: center !important;
    gap: 4px !important;
    padding: 0 12px !important;
}

/* Each nav link */
[data-testid="stHeaderNavItems"] a,
div[data-testid="stTopNavItems"] a,
[data-testid="stHeaderNavLink"] {
    text-decoration: none !important;
    color: #111111 !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    padding: 8px 12px !important;
    border-radius: 8px !important;
    transition: background 0.2s ease !important;
    white-space: nowrap !important;
    background: transparent !important;
}

[data-testid="stHeaderNavItems"] a:hover,
div[data-testid="stTopNavItems"] a:hover,
[data-testid="stHeaderNavLink"]:hover {
    background: #f1f1f1 !important;
    color: #111111 !important;
}

/* Active nav link */
[data-testid="stHeaderNavItems"] a[aria-current="page"],
div[data-testid="stTopNavItems"] a[aria-selected="true"],
[data-testid="stHeaderNavLink"][aria-current="page"] {
    background: #111111 !important;
    color: #ffffff !important;
    border-radius: 8px !important;
}

/* App logo / brand area in the header */
[data-testid="stLogoImage"],
[data-testid="stAppViewBlockContainer"] ~ header img {
    height: 32px !important;
}

/* ── Page content container ── */
.stApp > div[data-testid="block-container"],
div[data-testid="block-container"],
.stMainBlockContainer,
.main .block-container {
    padding-top: 1.5rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    max-width: 100% !important;
    width: 100% !important;
    background: #030814 !important;
}

/* ── Shared content classes ── */
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
.page-title {
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 8px 0;
}
.page-subtitle {
    font-size: 16px;
    color: #b9c4d6;
    margin-bottom: 32px;
    line-height: 1.6;
}
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
.pub-title { font-size: 18px; font-weight: 800; color: #ffffff; margin: 0 0 10px 0; line-height: 1.4; }
.pub-authors { font-size: 14px; color: #b9c4d6; margin: 0 0 8px 0; line-height: 1.6; }
.pub-journal { font-size: 14px; color: #7ea8d8; font-style: italic; margin: 0 0 6px 0; }
.pub-doi { font-size: 13px; color: #4b6580; margin: 0 0 16px 0; }
.pub-doi span { color: #5b8fbf; }
.pub-btn {
    display: inline-block; text-decoration: none;
    font-size: 13px; font-weight: 700; padding: 7px 18px;
    border-radius: 8px; border: 1px solid #1b263c;
    color: #d9e3f3; background: #111c30;
    transition: background 0.2s ease, border-color 0.2s ease;
}
.pub-btn:hover { background: #1a2f52; border-color: #3b82f6; color: #ffffff; }

.footer-wrap { margin: 0 auto; color: #ffffff; padding-top: 1rem; }
.stMarkdown, .stText, p, span, label, div { color: inherit; }

@media (max-width: 600px) {
    .page-title { font-size: 24px; }
    .description-text { font-size: 14px; padding: 12px; }
}
</style>
""", unsafe_allow_html=True)

# ==============================
# Navigation — Streamlit handles routing natively
# ==============================
 pg = st.navigation([
    #st.Page("exploration.py", title="Explore"),
    st.Page("about.py",       title="About"),
    st.Page("Team.py",        title="Team"),
    st.Page("Publications.py", title="Publications"),
], position="top")

pg.run()
