from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem  # noqa: F401
import streamlit as st

st.set_page_config(
    page_title="SmilX",
    page_icon="🧪",
    layout="wide"
)

# =========================
# CSS 
# =========================
st.markdown("""
<style>
/* Espaciado general */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1rem;
    max-width: 100%;
}

/* Ocultar elementos por defecto de Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Tarjeta superior */
.hero-card {
    padding: 1.25rem 1.5rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #f8fbff 0%, #eef6ff 100%);
    border: 1px solid #dbeafe;
    margin-bottom: 1rem;
}

/* Texto principal */
.hero-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
    color: #0f172a;
}

.hero-subtitle {
    font-size: 1rem;
    color: #475569;
    margin-bottom: 0;
}

/* Caja descriptiva */
.description-box {
    padding: 1rem 1.2rem;
    border-radius: 16px;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
    margin-top: 1rem;
    margin-bottom: 1rem;
    color: #334155;
    line-height: 1.7;
    text-align: justify;
}

/* Footer */
.footer-box {
    text-align: center;
    color: #64748b;
    font-size: 0.95rem;
    padding-top: 0.5rem;
}
</style>
""", unsafe_allow_html=True)


def render_topbar():
    """
    Barra superior usando componentes nativos de Streamlit.
    No usa HTML para navbar.
    """
    col1, col2, col3, col4, col5, col6 = st.columns([1.2, 1.2, 1.2, 1.2, 4, 1.2])

    with col1:
        if st.button("Home", use_container_width=True):
            st.session_state["section"] = "Home"

    with col2:
        if st.button("About us", use_container_width=True):
            st.session_state["section"] = "About us"

    with col3:
        if st.button("Program", use_container_width=True):
            st.session_state["section"] = "Program"

    with col4:
        if st.button("Publications", use_container_width=True):
            st.session_state["section"] = "Publications"

    with col6:
        st.link_button(
            "GitHub",
            "https://github.com/LuisOrz/SmilX",
            use_container_width=True
        )


def render_header():
    st.markdown("""
    <div class="hero-card">
        <div class="hero-title">SmilX</div>
        <p class="hero-subtitle">
            Open-source platform for generating and exploring chemical representations using SMILES.
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_home():
    st.subheader("Chemical Space Generation")

    a = initial_parameters()

    with st.spinner("Please wait..."):
        _ = chemical_space(a)

    st.markdown("""
    <div class="description-box">
    By integrating five syntactic constraints—including branch limitations,
    balanced parentheses, and aromaticity exclusion—TokenSMILES minimizes
    redundant enumerations for alkanes and ensures valence and octet rule
    compliance through semantic parsing. Implemented in SmilX, an open-source
    tool, TokenSMILES successfully generates SMILES for classical organic systems.
    </div>
    """, unsafe_allow_html=True)


def render_about():
    st.subheader("About us")
    st.write(
        """
        SmilX is an open-source initiative focused on the generation, parsing,
        and exploration of chemical structures represented through SMILES.
        The project aims to provide accessible tools for education, research,
        and chemical informatics workflows.
        """
    )

    st.info(
        "This section can include your team, institutional affiliations, project goals, and contact information."
    )


def render_program():
    st.subheader("Program")
    st.write(
        """
        In this section, you can describe the workflow of SmilX:
        parameter definition, chemical space generation, molecular validation,
        visualization, and export of generated structures.
        """
    )

    tabs = st.tabs(["Workflow", "Features", "Applications"])

    with tabs[0]:
        st.write("""
        1. Define initial molecular constraints.  
        2. Generate valid candidate SMILES.  
        3. Filter structures according to syntactic and semantic rules.  
        4. Explore resulting chemical space.
        """)

    with tabs[1]:
        st.write("""
        - SMILES generation  
        - Constraint-based enumeration  
        - Chemical space exploration  
        - Open-source reproducibility
        """)

    with tabs[2]:
        st.write("""
        SmilX can be useful in chemistry education, cheminformatics,
        molecular design exercises, and exploratory computational studies.
        """)


def render_publications():
    st.subheader("Publications")
    st.write(
        """
        Here you can place associated articles, conference papers, preprints,
        or documentation related to TokenSMILES and SmilX.
        """
    )

    st.warning("Add publication cards, DOI links, BibTeX references, or PDFs here.")


def render_footer():
    st.divider()
    st.markdown("""
    <div class="footer-box">
        Web Designers: Gabriela Yasmin Vidales Ayala & José Emmanuel Soberanis Cáceres
    </div>
    """, unsafe_allow_html=True)


def main():
    if "section" not in st.session_state:
        st.session_state["section"] = "Home"

    render_topbar()
    st.write("")
    render_header()

    section = st.session_state["section"]

    if section == "Home":
        render_home()
    elif section == "About us":
        render_about()
    elif section == "Program":
        render_program()
    elif section == "Publications":
        render_publications()

    render_footer()


if __name__ == "__main__":
    main()
