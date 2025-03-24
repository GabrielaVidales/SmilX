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
            z-index: 100;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 10px 0 10px 20px;
            margin: 0;
        }
        
        .navbar-container {
            display: flex;
            gap: 20px;
            align-items: center;
            width: 100%;
        }
        
        .navbar a {
            color: black;
            text-align: left;
            padding: 12px 16px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 700; /* Texto en negrita */
            transition: all 0.3s ease;
            border-radius: 4px;
            white-space: nowrap;
        }
        
        .navbar a:hover {
            background-color: #f0f0f0;
            color: black;
        }
        
        .navbar a.active {
            background-color: #f0f0f0;
        }
        
        .content {
            margin-top: 70px;
        }
        
        /* Ocultar el menú por defecto de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Eliminar márgenes por defecto */
        .stApp {
            margin: 0;
            padding: 0;
        }
        
        /* Eliminar padding del contenedor principal */
        .main .block-container {
            padding-top: 0;
        }
    </style>
""", unsafe_allow_html=True)

# HTML para el menú de navegación
st.markdown("""
    <div class="navbar">
        <div class="navbar-container">
            <a href="/" target="_self">Home</a>
            <a href="#about" target="_self">Sobre nosotros</a>
            <a href="#program" target="_self">Programa</a>
            <a href="#publications" target="_self">Publicaciones</a>
            <a href="#support" target="_self">Soporte técnico</a>
        </div>
    </div>
    <div class="content"></div>
""", unsafe_allow_html=True)

def main():
    # Inicializar parámetros
    a = initial_parameters()
    
    with st.spinner("Please wait...", show_time=True):
        b = chemical_space(a)

    st.markdown("<br>"*5, unsafe_allow_html=True)
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

