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

    .footer-wrap { margin: 0 auto; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)


def render_nav(active: str):
    inject_base_css()

    page_urls = {
        "Explore": "/",
        "About": "/About",
        "Team": "/Team",
        "Publications": "/Publications",
    }

    nav_items_html = ""
    for label, url in page_urls.items():
        is_active = label == active
        active_class = "active" if is_active else ""
        nav_items_html += f'<a href="{url}" class="nav-link {active_class}">{label}</a>\n'

    st.markdown(f"""
    <style>
    .smilx-navbar {{
        position: sticky;
        top: 0;
        z-index: 9999;
        background: #ffffff;
        border-bottom: 1px solid #e8e8e8;
        box-shadow: 0 2px 8px rgba(0,0,0,0.10);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 24px;
        min-height: 56px;
        margin: 0 -1rem 1.2rem -1rem;
        box-sizing: border-box;
        width: calc(100% + 2rem);
    }}
    .nav-brand {{
        font-size: 20px;
        font-weight: 800;
        color: #111111;
        white-space: nowrap;
        text-decoration: none;
    }}
    .nav-links {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .nav-link {{
        display: inline-block;
        padding: 6px 16px;
        border-radius: 10px;
        background: #ffffff;
        color: #111111 !important;
        font-weight: 700;
        text-decoration: none !important;
        border: 1px solid #d9d9d9;
        font-size: 14px;
        transition: background 0.15s, color 0.15s;
        cursor: pointer;
    }}
    .nav-link:hover {{
        background: #f0f0f0 !important;
        color: #111111 !important;
    }}
    .nav-link.active {{
        background: #111111 !important;
        color: #ffffff !important;
        border-color: #111111 !important;
        cursor: default;
        pointer-events: none;
    }}
    .nav-github {{
        font-size: 24px;
        text-decoration: none;
        line-height: 1;
    }}
    </style>

    <div class="smilx-navbar">
        <a href="/" class="nav-brand">SmilX</a>
        <div class="nav-links">
            {nav_items_html}
        </div>
        <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener" class="nav-github">&#x1F419;</a>
    </div>
    """, unsafe_allow_html=True)
