<p align="center">
  <img src="https://github.com/LuisOrz/SmilX/blob/main/logo_smilx.png" width="220">
</p>

<h1 align="center">
SMILX
</h1>

<p align="center">
<b>Grammar-Driven SMILES Standardization and Molecular Structure Generation</b>
</p>

<p align="center">
Computational Chemistry • Cheminformatics • Molecular Enumeration
</p>

---

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![RDKit](https://img.shields.io/badge/RDKit-Compatible-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-GPLv3-orange)
![Status](https://img.shields.io/badge/Status-Research-purple)

</p>

---

# SMILX (TokenSMILES Framework)

Repositorio oficial del proyecto:

### Grammar-Driven SMILES Standardization with TokenSMILES

Desarrollado en:

**Centro de Investigación y Estudios Avanzados (CINVESTAV) Mérida**

---

<p align="center">

Desarrollado por  

<span style="background:#ff4d88;color:white;padding:4px 10px;border-radius:6px;">Luis Armando Gonzalez-Ortiz</span>  
<span style="background:#ff4d88;color:white;padding:4px 10px;border-radius:6px;">Lisset Noriega</span>  
<span style="background:#ff4d88;color:white;padding:4px 10px;border-radius:6px;">Filiberto Ortiz</span>  
<span style="background:#ff4d88;color:white;padding:4px 10px;border-radius:6px;">Gabriela Vidales-Ayala</span>  
<span style="background:#ff4d88;color:white;padding:4px 10px;border-radius:6px;">Emmanuel Soberanis</span>  
<span style="background:#ff4d88;color:white;padding:4px 10px;border-radius:6px;">Amilcar Meneses</span>  
<span style="background:#ff4d88;color:white;padding:4px 10px;border-radius:6px;">Alan Aspuru-Guzik</span>  
<span style="background:#ff4d88;color:white;padding:4px 10px;border-radius:6px;">Gabriel Merino</span>

</p>

---

# Overview

**SMILX** is a grammar-driven framework for generating and standardizing molecular structures using the **SMILES chemical representation**.

The system constructs chemically valid molecules directly from **molecular formulas**, using algorithmic rules that simulate chemical grammar.

The approach ensures:

• valid valence states  
• correct unsaturation patterns  
• cycle detection  
• controlled heteroatom substitution  
• systematic enumeration of chemical structures  

---

# Features

SMILX provides tools for:

• Molecular formula parsing  
• Hydrogen Deficiency Index (HDI) computation  
• Unsaturation configuration generation  
• Grammar-based SMILES construction  
• Double and triple bond insertion  
• Cycle detection and ring formation  
• Heteroatom substitution (N, O, S, P, B, halogens)  
• Streamlit interface for interactive exploration  

---

# Installation

Clone the repository:

```bash
git clone https://github.com/LuisOrz/SmilX.git
cd SmilX
