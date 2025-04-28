from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem
import streamlit as st

st.set_page_config(
    page_title="SmilX",
    layout="wide"
)

# CSS personalizado para el menú
st.markdown("""
    <style>
        /* Estilos del navbar */
        .navbar {
            background-color: white;
            overflow: hidden;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 60px;
            z-index: 1000;
            box-shadow: 0 8px 10px -1px rgba(0,0,0,0.1); /* Sombra más pronunciada abajo */
            display: flex;
            align-items: center;
            padding: 0 10px; 
            margin: 0;
            border-bottom: 1px solid #f0f0f0; 
        }
        
        .navbar-container {
            display: flex;
            gap: 15px;
            align-items: center;
            width: 100%;
            max-width: 1200px; 
            margin: 0 auto;
            padding: 0;
        }
        
        .navbar a {
            color: black;
            text-align: left;
            marging-left: -400px;
            padding: 12px 16px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 700;
            transition: all 0.3s ease;
            border-radius: 10px;
            white-space: nowrap;
            height: 100%;
            display: flex;
            align-items: center;
        }
        
        .navbar a:hover {
            background-color: #f0f0f0;
            color: black;
        }
        
        .navbar a.active {
            background-color: #f0f0f0;
        }

        .github-icon {
            margin-left: auto;
            padding: 12px 16px;
        }
        .github-icon img {
            height: 30px;
            transition: transform 0.3s ease;
        }
        .github-icon img:hover {
            transform: scale(1.1);
            border-radius: 200px;
        }

        .github-icon:hover{
            transform: scale(1.1);
            border-radius: 200px;
        }
        
        /* Ajuste del contenido principal */
        .main .block-container {
            padding-top: 70px !important; 
        }
        
        /* Eliminar todos los espacios innecesarios */
        .stApp {
            margin: 0;
            padding: 0;
        }
        
        /* Ocultar el menú por defecto de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Ajustar el footer para que quede pegado */
        .footer {
            margin-top: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# HTML para el menú de navegación
st.markdown("""
    <nav class="navbar">
        <div class="navbar-container">
            <a href="/" target="_self">Home</a>
            <a href="#about" target="_self">About us</a>
            <a href="#program" target="_self">Program</a>
            <a href="#publications" target="_self">Publications</a>
            <div class="github-icon">
                <a href="https://github.com/LuisOrz/SmilX" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
                </a>
            </div>
        </div>
    </nav>
""", unsafe_allow_html=True)

def main():
    # Inicializar parámetros
    a = initial_parameters()
    
    with st.spinner("Please wait...", show_time=True):
        b = chemical_space(a)

    # Agregar el párrafo después de las moléculas que se muestran
    st.markdown("""
    By integrating five syntactic constraints—including branch limitations, balanced parentheses, and aromaticity exclusion—TokenSMILES minimizes redundant enumerations for alkanes and ensures valence and octet rule compliance through semantic parsing. Implemented in SmilX, an open-source tool, TokenSMILES successfully generates SMILES for classical organic systems.
    """)

    # Footer pegado al contenido
    st.markdown("<br>", unsafe_allow_html=True)
    footer = st.container()
    with footer:
        st.divider()
        st.markdown(
            """
            **Web Designers: Gabriela Yasmin Vidales Ayala & José Emmanuel Soberanis Cáceres**
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
