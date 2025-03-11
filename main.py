from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem
import streamlit as st

st.set_page_config(
    page_title = "SmilX",
    layout = wide
)

def main():
      
    # Inicializar parámetros
    a = initial_parameters()

    b = chemical_space(a)
    
    with open(f"{a.filename_output_smi}", "r") as file:
        st.download_button(
            label="Download SMILES",
            data=file,
            file_name=f"{a.filename_output_smi}",
            mime="text/smi",
        )

if __name__ == "__main__":
    main()


