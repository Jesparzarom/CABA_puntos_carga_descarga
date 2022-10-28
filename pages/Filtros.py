import streamlit as st
import streamlit.components.v1 as components
from General import seleccion, dataset2
from map_generator.mapa import mapa



# --- STREAMLIT---

st.set_page_config(
    page_title="Puntos de Carga y Descarga en CABA",
    page_icon=":truck:",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        "Get Help": "https://github.com/Jesparzarom/CABA_puntos_carga_descarga",
        "Report a bug": "https://github.com/Jesparzarom/CABA_puntos_carga_descarga",
        "About": "## Powered by Python.:snake: ```Autor: J. Esparza R.``` ",
    },
)

st.sidebar.markdown("# Datos Filtrados")
st.sidebar.write(''' En esta página puedes interactuar
                 un poco con los datos. ''')

Barrio = st.sidebar.selectbox("Selecciona un barrrio",
                                options=dataset2["barrio"].unique(),
                                index=3,)
seleccion = dataset2.query("barrio == @Barrio")
                              
                        
#   Filtros
st.markdown("###### <-- Despliega el menú para ver las opciones")
st.subheader("Mapa interactivo")
grupos = dataset2.groupby(["barrio"])["lat", "long"].mean()
grupos = grupos.values.tolist()


mapa(seleccion, grupos)
p = open("Templates\mapa.html")
components.html(p.read(), height=400)

if seleccion["barrio"].count() != 1935:
    left, right = st.columns(2)
    with left:
        components.html(
            f"""                    
                        <div style="text-align:center;">
                        <h3 style="color:teal;">Barrio:</h3>
                        <hr>
                        <h2>
                            <span style="color:tomato; font-size:40px; letter-spacing:-3px;">
                                {Barrio}
                            </span>
                        </h2>
                        </div>"""
        )

    with right:
        components.html(
            f"""
                        <div style="text-align:center;">
                        <h3 style="color:teal;">Puntos de C. y D. totales:</h3>
                        <hr>
                        <h2>
                            <span style="color:tomato; font-size:40px; letter-spacing:-3px;">
                                {(seleccion["barrio"].count())}
                            </span>
                        </h2>
                        </div>"""
        )