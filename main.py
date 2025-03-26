from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem
import streamlit as st

st.set_page_config(
    page_title="SmilX",
    layout="wide"
)

# CSS personalizado para el menú y el footer
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
            height: 70px;
            z-index: 1000;
            box-shadow: 0 8px 10px -1px rgba(0,0,0,0.1); /* Sombra más pronunciada abajo */
            display: flex;
            align-items: center;
            padding: 0 20px; 
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
            justify-content: flex-start; /* Alinea el contenido a la izquierda */
        }
        
        .navbar a {
            color: black;
            text-align: left;
            padding: 12px 16px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 700;
            transition: all 0.3s ease;
            border-radius: 4px;
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
        
        /* Ajuste del contenido principal */
        .main .block-container {
            padding-top: 70px !important; 
        }
        
        /* Eliminar todos los espacios innecesarios */
        .stApp {
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        
        /* Ocultar el menú por defecto de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Estilos del footer */
        .footer {
            background-color: white;
            text-align: center;
            padding: 10px 20px;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            border-top: 1px solid #f0f0f0;
            box-shadow: 0 -8px 10px -1px rgba(0,0,0,0.1); /* Sombra más pronunciada arriba */
        }
    </style>
""", unsafe_allow_html=True)

# HTML para el menú de navegación y el footer
st.markdown("""
    <nav class="navbar">
        <div class="navbar-container">
            <a href="/" target="_self">Home</a>
            <a href="#about" target="_self">About Us</a>
            <a href="#program" target="_self">Program</a>
            <a href="#publications" target="_self">Publications</a>
        </div>
    </nav>
    <div class="footer">
        <p>Web Designers: Gabriela Yasmin Vidales Ayala & José Emmanuel Soberanis Cáceres</p>
    </div>
""", unsafe_allow_html=True)

def main():
    # Inicializar parámetros
    a = initial_parameters()
    
    with st.spinner("Please wait...", show_time=True):
        b = chemical_space(a)

if __name__ == "__main__":
    main()
