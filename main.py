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


from shared_nav import render_nav

render_nav("Explore")



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
