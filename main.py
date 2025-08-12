from smilx_parameters import initial_parameters
from smilx_chemical_space import chemical_space
from rdkit import Chem  # noqa: F401 (si no se usa directamente)
import streamlit as st

# Config de página — debe ir antes de cualquier salida
st.set_page_config(
    page_title="SmilX",
    layout="wide"
)

# CSS global para forzar ancho completo y corregir desplazamientos
st.markdown("""
<style>
/* ====== Reset de layout para ancho completo ====== */
/* Contenedor principal de Streamlit */
.stApp > div[data-testid="block-container"]{
    max-width: 100% !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-top: 70px !important; /* espacio por navbar fijo */
}

/* Cualquier bloque vertical/columna debe poder expandirse */
.stApp [data-testid="stVerticalBlock"],
.stApp [data-testid="stHorizontalBlock"],
.stApp [data-testid="column"],
.stApp [data-testid="stContainer"]{
    width: 100% !important;
    max-width: 100% !important;
    flex: 1 1 auto !important;
}

/* Elementos gráficos: que ocupen el ancho disponible sin desbordar */
.stApp svg,
.stApp canvas,
.stApp img,
.stApp .plot-container,
.stApp .element-container,
.stApp .stMarkdown div{
    max-width: 100% !important;
    width: 100% !important;
}

/* Evitar márgenes/padding inesperados a nivel app */
.stApp{
    margin: 0 !important;
    padding: 0 !important;
}

/* ====== Navbar fijo arriba ====== */
.navbar{
    background-color: white;
    overflow: hidden;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px;
    z-index: 1000;
    box-shadow: 0 8px 10px -1px rgba(0,0,0,0.1);
    display: flex;
    align-items: center;
    padding: 0 10px;
    margin: 0;
    border-bottom: 1px solid #f0f0f0;
}

/* Contenedor del navbar: ya no limitamos a 1200px */
.navbar-container{
    display: flex;
    gap: 12px;
    align-items: center;
    width: 100%;
    margin: 0;
    padding: 0;
}

/* Enlaces del navbar */
.navbar a{
    color: black;
    text-align: left;
    padding: 12px 16px;
    text-decoration: none;
    font-size: 16px;
    font-weight: 700;
    transition: all .3s ease;
    border-radius: 10px;
    white-space: nowrap;
    height: 100%;
    display: flex;
    align-items: center;
}

.navbar a:hover{
    background-color: #f0f0f0;
    color: black;
}

.navbar a.active{
    background-color: #f0f0f0;
}

/* GitHub a la derecha */
.github-icon{
    margin-left: auto;
    padding: 12px 16px;
}

.github-icon img{
    height: 30px;
    transition: transform .3s ease;
}

.github-icon img:hover,
.github-icon:hover{
    transform: scale(1.1);
    border-radius: 200px;
}

/* ====== Ajustes específicos útiles para la grilla de moléculas ====== */
/* Si la vista de isómeros usa un contenedor tipo grid genérico,
   estas reglas asegurarán que fluya a todo el ancho. */

.molecule-grid, .isomer-grid, .cards-grid{
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)) !important;
    gap: 1rem !important;
    width: 100% !important;
}

.molecule-card, .isomer-card, .card{
    width: 100% !important;
}

/* ====== Ocultar menú/encabezado por defecto ====== */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Footer pegado al contenido */
.footer{ margin-top: 0 !important; }
</style>
""", unsafe_allow_html=True)

# HTML del menú de navegación (fijo)
st.markdown("""
<nav class="navbar">
    <div class="navbar-container">
        <a href="/" target="_self">Home</a>
        <a href="#about" target="_self">About us</a>
        <a href="#program" target="_self">Program</a>
        <a href="#publications" target="_self">Publications</a>
        <div class="github-icon">
            <a href="https://github.com/LuisOrz/SmilX" target="_blank" rel="noopener">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            </a>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)


def main():
    # Inicializar parámetros
    a = initial_parameters()

    # Spinner (sin argumento show_time; no es válido en Streamlit)
    with st.spinner("Please wait..."):
        _ = chemical_space(a)

    # Texto posterior a la visualización
    st.markdown("""
By integrating five syntactic constraints—including branch limitations, balanced parentheses, and aromaticity exclusion—TokenSMILES minimizes redundant enumerations for alkanes and ensures valence and octet rule compliance through semantic parsing. Implemented in SmilX, an open-source tool, TokenSMILES successfully generates SMILES for classical organic systems.
""")

    # Footer
    st.markdown("<br>", unsafe_allow_html=True)
    footer = st.container()
    with footer:
        st.divider()
        st.markdown(
            "**Web Designers: Gabriela Yasmin Vidales Ayala & José Emmanuel Soberanis Cáceres**",
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()
