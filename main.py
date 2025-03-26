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
            <a href="#about" target="_self">Sobre nosotros</a>
            <a href="#program" target="_self">Programa</a>
            <a href="#publications" target="_self">Publicaciones</a>
        </div>
    </nav>
""", unsafe_allow_html=True)

def main():
    # Inicializar parámetros
    a = initial_parameters()
    
    with st.spinner("Please wait...", show_time=True):
        b = chemical_space(a)

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
He realizado los siguientes cambios:

Eliminado el padding innecesario en la clase .navbar.
Reducido el grosor del borde inferior de la barra de navegación.
Eliminado el padding innecesario en la clase .navbar-container.
Espero que estos cambios mejoren la apariencia y el rendimiento de tu barra de menú. ¿Hay algo más en lo que pueda ayudarte?


Editar en Pages




El contenido generado por la inteligencia artificial puede ser incorrecto
You said:

haz que el texto del menú esté más alineado al lado izquierdo y pasa a inglés las etiquetas. 
Copilot said:
Copilot
¡Claro! Aquí tienes el código actualizado con las etiquetas en inglés y el texto del menú alineado más a la izquierda:

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
            <a href="#about" target="_self">About Us</a>
            <a href="#program" target="_self">Program</a>
            <a href="#publications" target="_self">Publications</a>
        </div>
    </nav>
""", unsafe_allow_html=True)

def main():
    # Inicializar parámetros
    a = initial_parameters()
    
    with st.spinner("Please wait...", show_time=True):
        b = chemical_space(a)

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

if __name__ ==
