<p align="center">
  <img src="https://github.com/LuisOrz/SmilX/blob/main/logo_smilx.png" width="240">
</p>

<h1 align="center">
SMILX (TokenSMILES Framework)
</h1>

<p align="center">
<b>Grammar-Constrained Chemical Space Exploration for Isomers using SMILES</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![RDKit](https://img.shields.io/badge/RDKit-Compatible-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-GPLv3-orange)
![Status](https://img.shields.io/badge/Status-Research-purple)

</p>

---

## What is SMILX?

**SMILX is a software to explore the chemical space of isomers using the SMILES language under grammar constraints.**  
Given a **molecular formula**, SMILX systematically constructs chemically valid molecular graphs by applying a **grammar-driven generation process**, ensuring consistent structural rules (valence, connectivity, unsaturation, and ring closures) while enumerating candidate isomers.

This repository contains the **official implementation** of the SMILX / TokenSMILES framework, developed at:

**Centro de Investigación y Estudios Avanzados (CINVESTAV) Mérida**

---

## Key Features

- Molecular formula parsing (e.g., `C6H6`, `C2H5NO2`)
- Hydrogen Deficiency Index (HDI) computation
- Enumeration of valid unsaturation patterns (double bonds, triple bonds, rings)
- Grammar-based construction of carbon skeletons and branching
- Cycle formation (ring closures) with validity checks
- Heteroatom substitution under valence constraints  
  Supported: `N O S P B F Cl Br I`
- Interactive exploration via **Streamlit**
- RDKit-friendly workflow for downstream cheminformatics tasks

---

## Installation

Clone the repository:

```bash
git clone https://github.com/LuisOrz/SmilX.git
cd SmilX

Create and activate a virtual environment (recommended):

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Run (Streamlit App)

Launch the interactive interface:

streamlit run app.py

Example molecular formulas:

C6H6
C2H5NO2
C7H8O

Typical workflow:

Parse molecular formula

Compute HDI

Generate possible unsaturation configurations

Construct grammar-constrained carbon skeletons

Apply bond/ring transformations and substitutions

Output standardized SMILES (and auxiliary formats if enabled)

Project Structure
SMILX
│
├── logo_smilx.png
├── requirements.txt
├── packages.txt
│
├── smilx_parameters.py
├── smilx_chemistry_tools.py
│
└── app.py
Core Modules

smilx_chemistry_tools.py
Core algorithms for unsaturation enumeration, grammar-based SMILES construction, bond transformations, cycle detection, and atom replacement.

smilx_parameters.py
Streamlit UI, molecular formula parsing, parameter initialization, and generation setup.

Applications

SMILX can be used for:

Chemical space exploration (isomer enumeration)

Computational chemistry workflows

Cheminformatics research

Dataset generation for machine learning

Systematic structure generation from molecular formulas

Authors

Developed by:

Luis Armando Gonzalez-Ortiz

Lisset Noriega

Filiberto Ortiz-Chi

Gabriela Vidales-Ayala

Emmanuel Soberanis-Cáceres

Amilcar Meneses-Viveros

Alan Aspuru-Guzik

Gabriel Merino

CINVESTAV Mérida

License

GNU General Public License v3.0

Citation

If you use this software in academic work, please cite:

Gonzalez-Ortiz, L. A.; Noriega, L.; Ortiz-Chi, F.; Vidales-Ayala, G.; Soberanis-Cáceres, E.; Meneses-Viveros, A.; Aspuru-Guzik, A.; Merino, G.
Grammar-driven SMILES standardization with TokenSMILES. Chemical Science, 2026, 17, 1666–1675.
DOI: https://doi.org/10.1039/D5SC05004A
