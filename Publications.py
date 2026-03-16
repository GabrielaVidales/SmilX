import streamlit as st

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
# Page content
# ==============================
st.markdown('<div class="page-title">Publications 📑</div>', unsafe_allow_html=True)

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
