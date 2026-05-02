import streamlit as st

def inject_base_css():
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

    .nav-wrap {
        margin: 0 -1rem 1.2rem -1rem;
        position: sticky;
        top: 0;
        z-index: 9999;
    }
    .navbar {
        min-height: 56px;
        background: #ffffff;
        border-bottom: 1px solid #e8e8e8;
        display: flex;
        align-items: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.10);
        width: 100%;
        padding: 8px 24px;
        box-sizing: border-box;
    }
    .brand {
        font-size: 20px;
        font-weight: 800;
        color: #111111;
        white-space: nowrap;
    }
    .footer-wrap { margin: 0 auto; color: #ffffff; }

    .stPageLink a {
        display: block;
        text-align: center;
        padding: 0.45rem 0.8rem;
        border-radius: 10px;
        background: #ffffff;
        color: #111111 !important;
        font-weight: 700;
        text-decoration: none !important;
        border: 1px solid #d9d9d9;
    }

    .stButton > button {
        border-radius: 10px !important;
        border: 1px solid #111111 !important;
        background: #111111 !important;
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    </style>
    """, unsafe_allow_html=True)


def render_nav(active: str):
    inject_base_css()

    st.markdown('<div class="nav-wrap"><div class="navbar">', unsafe_allow_html=True)
    cols = st.columns([1.2, 1, 1, 1, 1, 0.5])

    with cols[0]:
        st.markdown('<div class="brand">SmilX</div>', unsafe_allow_html=True)

    targets = [
        ("Explore", "main.py"),
        ("About", "pages/1_About.py"),
        ("Team", "pages/2_Team.py"),
        ("Publications", "pages/3_Publications.py"),
    ]

    for i, (label, target) in enumerate(targets, start=1):
        with cols[i]:
            if label == active:
                st.button(label, key=f"nav_{label}", disabled=True, use_container_width=True)
            else:
                st.page_link(target, label=label, use_container_width=True)

    with cols[5]:
        st.markdown(
            '<div style="text-align:right;"><a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener" style="text-decoration:none;font-size:24px;">🐙</a></div>',
            unsafe_allow_html=True,
        )

    st.markdown('</div></div>', unsafe_allow_html=True)
