```{=html}
<p align="center">
```
`<img src="https://github.com/LuisOrz/SmilX/blob/main/logo_smilx.png" width="240">`{=html}
```{=html}
</p>
```
```{=html}
<h1 align="center">
```
SMILX (TokenSMILES Framework)
```{=html}
</h1>
```
```{=html}
<p align="center">
```
`<b>`{=html}Grammar-Constrained Chemical Space Exploration for Isomers
using SMILES`</b>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![RDKit](https://img.shields.io/badge/RDKit-Compatible-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-GPLv3-orange)
![Status](https://img.shields.io/badge/Status-Research-purple)

```{=html}
</p>
```

------------------------------------------------------------------------

## Web Application

The interactive version of **SMILX** is available online:

https://smilx-isogenerator.streamlit.app/

This web interface allows users to explore the chemical space of isomers
directly from a molecular formula without installing the software
locally.

------------------------------------------------------------------------

## What is SMILX?

**SMILX is a software designed to explore the chemical space of isomers
using the SMILES language under grammar constraints.**

Given a **molecular formula**, SMILX systematically constructs
chemically valid molecular graphs by applying a **grammar-driven
generation process**. The algorithm ensures structural consistency with
respect to chemical rules such as:

-   valence constraints\
-   connectivity\
-   unsaturation patterns\
-   ring closures

This approach allows the systematic enumeration of candidate molecular
isomers.

This repository contains the **official implementation of the SMILX /
TokenSMILES framework**, developed at:

**Centro de Investigación y Estudios Avanzados (CINVESTAV) Mérida**

------------------------------------------------------------------------

## Key Features

-   Molecular formula parsing (e.g., `C6H6`, `C2H5NO2`)
-   Hydrogen Deficiency Index (HDI) computation
-   Enumeration of valid unsaturation patterns (double bonds, triple
    bonds, rings)
-   Grammar-based construction of carbon skeletons and branching
-   Cycle formation (ring closures) with validity checks
-   Heteroatom substitution under valence constraints\
    Supported elements:

```{=html}
<!-- -->
```
    N O S P B F Cl Br I

-   Interactive exploration through **Streamlit**
-   RDKit-compatible workflow for downstream cheminformatics tasks

------------------------------------------------------------------------

## Installation

Clone the repository:

``` bash
git clone https://github.com/LuisOrz/SmilX.git
cd SmilX
```

Create and activate a virtual environment:

``` bash
python -m venv venv
```

Activate the environment:

**Linux / macOS**

``` bash
source venv/bin/activate
```

**Windows**

``` bash
venv\Scripts\activate
```

Install the required dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Running the Application Locally

After installing the dependencies, you can launch the Streamlit
interface with:

``` bash
streamlit run app.py
```

The application will open in your browser, where you can input molecular
formulas such as:

    C6H6
    C2H5NO2
    C7H8O

SMILX will automatically:

1.  Parse the molecular formula\
2.  Compute the Hydrogen Deficiency Index (HDI)\
3.  Generate valid unsaturation configurations\
4.  Construct carbon skeletons using grammar rules\
5.  Introduce bonds, cycles, and heteroatom substitutions\
6.  Output valid SMILES representations of candidate isomers

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

### Core Modules

**smilx_chemistry_tools.py**

Implements the core chemical algorithms responsible for:

-   unsaturation generation\
-   grammar-based SMILES construction\
-   bond manipulation\
-   cycle detection\
-   heteroatom substitution

------------------------------------------------------------------------

**smilx_parameters.py**

Handles:

-   molecular formula parsing\
-   parameter initialization\
-   Streamlit interface configuration\
-   syntax rule generation

------------------------------------------------------------------------

## Authors

Developed by:

-   Luis Armando Gonzalez-Ortiz\
-   Lisset Noriega\
-   Filiberto Ortiz-Chi\
-   Gabriela Vidales-Ayala\
-   Emmanuel Soberanis-Cáceres\
-   Amilcar Meneses-Viveros\
-   Alan Aspuru-Guzik\
-   Gabriel Merino

Centro de Investigación y Estudios Avanzados (CINVESTAV) Mérida

------------------------------------------------------------------------

## License

This project is distributed under the **GNU General Public License v3.0
(GPL-3.0)**.

------------------------------------------------------------------------

## Citation

If you use SMILX in scientific research, please cite:

Gonzalez-Ortiz, L. A.; Noriega, L.; Ortiz-Chi, F.; Vidales-Ayala, G.;\
Soberanis-Cáceres, E.; Meneses-Viveros, A.; Aspuru-Guzik, A.; Merino, G.

**Grammar-driven SMILES standardization with TokenSMILES**

Chemical Science, 2026, 17, 1666--1675.\
https://doi.org/10.1039/D5SC05004A

------------------------------------------------------------------------

```{=html}
<p align="center">
```
⭐ If you find this repository useful for your research, consider giving
it a star.

```{=html}
</p>
```

