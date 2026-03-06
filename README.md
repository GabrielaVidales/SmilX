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
<a href="https://smilx-isogenerator.streamlit.app/">
🌐 Try the Web App
</a>
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

**SMILX is a software designed to explore the chemical space of isomers using the SMILES language under grammar constraints.**

Given a **molecular formula**, SMILX systematically constructs chemically valid molecular graphs by applying a **grammar-driven generation process**, ensuring consistency with chemical rules such as:

- valence constraints  
- connectivity  
- unsaturation patterns  
- ring closures  

This approach enables the systematic enumeration of candidate molecular isomers.

This repository contains the **official implementation of the SMILX / TokenSMILES framework**, developed at:

**Centro de Investigación y Estudios Avanzados (CINVESTAV) Mérida**

---

## Key Features

- Molecular formula parsing (e.g., `C6H6`, `C2H5NO2`)
- Hydrogen Deficiency Index (HDI) computation
- Enumeration of valid unsaturation patterns (double bonds, triple bonds, rings)
- Grammar-based construction of carbon skeletons and branching
- Cycle formation (ring closures) with validity checks
- Heteroatom substitution under valence constraints Supported elements: N O S P B F Cl Br I 
- Interactive exploration via **Streamlit**  
- RDKit-friendly workflow for downstream cheminformatics tasks

--- 

## Usage

SMILX can be used through the **online web application** or by running it locally.

### Online (recommended)

Use the web interface to explore molecular isomers directly from a molecular formula:

https://smilx-isogenerator.streamlit.app/

No installation is required.

---

### Run Locally

Clone the repository and install dependencies:

git clone https://github.com/LuisOrz/SmilX.git
cd SmilX

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

------------------------------------------------------------------------

## Project Structure

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

------------------------------------------------------------------------

## Authors

Developed by: Filiberto Ortiz, Gabriela Vidales-Ayala, Emmanuel Soberanis, Amilcar Meneses, Alan Aspuru-Guzik, and Gabriel Merino.
Centro de Investigación y Estudios Avanzados (CINVESTAV) Mérida

------------------------------------------------------------------------

## License

**GNU General Public License v3.0 (GPL-3.0)**

------------------------------------------------------------------------

## Citation

If you use SMILX in scientific research, please cite:

Gonzalez-Ortiz, L. A.; Noriega, L.; Ortiz-Chi, F.; Vidales-Ayala, G.; Soberanis-Cáceres, E.; Meneses-Viveros, A.; Aspuru-Guzik, A.; Merino, G. Grammar-driven SMILES standardization with TokenSMILES. Chemical Science, 2026, 17, 1666–1675. DOI: https://doi.org/10.1039/D5SC05004A

------------------------------------------------------------------------

