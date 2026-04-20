import streamlit as st
from shared_nav import render_nav

st.set_page_config(page_title="About | SmilX", layout="wide", initial_sidebar_state="collapsed")
render_nav("About")

st.markdown('<div class="page-title">About</div>', unsafe_allow_html=True)
st.markdown('''
<div class="about-card">
SmilX is an open-source platform for the generation and exploration of valid SMILES strings under syntactic and semantic constraints.
It integrates the TokenSMILES strategy to reduce redundant enumerations, enforce valence compliance, and support systematic exploration
of chemical space for classical organic systems and related representations.
</div>
<div class="about-card">
The platform is designed to be accessible, reproducible, and useful for education and research in computational chemistry,
cheminformatics, and molecular design.
</div>
''', unsafe_allow_html=True)

st.divider()
st.markdown('''<div class="footer-wrap"><b>Web Designers: Gabriela Yasmin Vidales Ayala &amp; José Emmanuel Soberanis Cáceres</b></div>''', unsafe_allow_html=True)
