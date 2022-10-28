import plotly_express as px
import streamlit as st
import streamlit.components.v1 as components
from map_generator.mapa import dataset, mapa



#   Modificando el dataset
dataset2 = dataset.drop(["calle_nombre", "calle_altura", 
                            "codigo_postal_argentino",
                            "codigo_postal"], axis=1)

dataset2 = dataset2.replace([r'Nu\u00f1ez'], 'Nuñez') # 'Nu\u00f1ez': demasiado raro dejarlo así.
dataset2 = dataset2.fillna("Sin dato") # No se borran las celdas vacías porque contienen ubicaciones.

dataset2 = dataset2.sort_values(by=['barrio'])
seleccion = dataset2.copy()



# Algunas variables de utilidad



# ------- COMIENZA STREAMLIT -------
#   Configuraciónes
st.set_page_config(page_title="Puntos de Carga y Descarga en CABA",
                   page_icon=":truck:",
                   layout="wide",
                   menu_items={'Get Help': 'https://github.com/Jesparzarom/CABA_puntos_carga_descarga', 
                               'Report a bug': "https://github.com/Jesparzarom/CABA_puntos_carga_descarga",
                               'About': 
                                   "## Powered by Python.:snake: ```Autor: J. Esparza R.``` "})
st.sidebar.markdown("Opciones")

# Header de la página
st.markdown('''
            # :truck: Puntos de Carga y Descarga
            ##### Habilitados para el transporte de mercadería en la ciudad de Buenos Aires
            ---
            # ''')


# Contenido: Filtros útiles y Dataframe del dataset en 2 columnas.
left, middle, right = st.columns(3)
with left:    
    components.html(f'''
                    <div style="text-align:center;">
                        <h3 style="color:teal;">Puntos totales en CABA:</h3>
                        <hr>
                        <h2>
                            <span style="color:tomato; font-size:40px; letter-spacing:-3px;">
                                {(seleccion["barrio"].count())}
                            </span>
                        </h2>
                    </div>''')
with middle:
    components.html(f'''
                    <div style="text-align:center;">
                        <h3 style="color:teal;">Barrios en CABA:</h3>
                        <hr>
                        <h2>
                            <span style="color:purple; font-size:40px; letter-spacing:-3px;">
                                48
                            </span>
                        </h2>
                    </div>''')   
with right:
    components.html(f'''
                    <div style="text-align:center;">
                        <h3 style="color:teal;">Promedio de puntos:</h3>
                        <hr>
                        <h2>
                            <span style="color:orange; font-size:40px; letter-spacing:-3px;">
                                {round(1935/48, 2)}
                            </span>
                        </h2>
                    </div>''') 
#   Mapa interactivo (Importado directamente del directorio ./Templates/)
st.subheader(":round_pushpin: Mapeo interactivo de los puntos")
p = open("Templates\mapa2.html")
components.html(p.read(), height=300)

st.subheader(":round_pushpin: Dashboard")
grafic_hoods = dataset2["barrio"]
grafico = px.bar(
    grafic_hoods,
    color=grafic_hoods,
    x="barrio",
    hover_name=None,
    orientation="v",
    log_x=False,
    log_y=False,
    width=800,
    height=500,
    title="GRAFICO DE PUNTOS DE CARGA Y DESCARGA POR BARRIO EN CABA",
    labels={"count": "", "color": "Barra"},
    template="plotly",
)

st.plotly_chart(grafico, use_container_width=True)