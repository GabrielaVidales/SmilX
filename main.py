from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem
import streamlit as st

st.set_page_config(
    page_title = "SmilX",
    layout = "wide"
)

def main():
      
    # Inicializar parámetros
    a = initial_parameters()
    
    with st.spinner("Please wait...", show_time=True):
        b = chemical_space(a)

if __name__ == "__main__":
    main()


