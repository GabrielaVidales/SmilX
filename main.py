from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem
import streamlit as st

def main():
      
    # Inicializar parámetros
    a = initial_parameters()

    b = chemical_space(a)

with open("logo_smilx.jpg", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="logo.jpg",
        mime="image/jpg",
    )

if __name__ == "__main__":
    main()
