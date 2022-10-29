import plotly_express as px
import streamlit as st
import streamlit.components.v1 as components
from map_generator.mapa import dataset



#   Modificando el dataset
dataset2 = dataset.drop(["calle_nombre", "calle_altura", 
                            "codigo_postal_argentino",
                            "codigo_postal"], axis=1)

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

st.sidebar.markdown("# Mapa General")

# Header de la página
components.html('''
            <header style="background: whitesmoke;">    
                <h1 style="font-size:5vw; padding:5px; border-radius:10px;">Puntos de Carga y Descarga</h1>
            </header> 
            ''')

#   Mapa interactivo (Importado directamente del directorio ./Templates/)
st.subheader(":pushpin: Mapeo interactivo de los puntos")
p = open("Templates\mapa2.html")
components.html(p.read(), height=300)

# Contenido: Filtros útiles y Dataframe del dataset en 2 columnas.
components.html(f'''
                <section style="display:flex; justify-content:space-evenly; text-shadow:1px 1px 10px rgba(0, 0, 0, 0.50); font-family:Lucida Grande;">
                
                    <div style="text-align:center; background: rgba(205, 134, 63, 0.20)">
                        <h5 style="color:teal;">Puntos totales<br> en CABA:</h5>
                        <h2>
                            <span style="color:aquamarine; font-size:4vw; ">
                                {(seleccion["barrio"].count())}
                            </span>
                        </h2>
                    </div>
                    
                    <div style="text-align:center; background: rgba(206, 0, 206, 0.20); padding:2px; ">
                        <h5 style="color:teal;">Barrios en<br> CABA:</h5>
                        <h2>
                            <span style="color:purple; font-size:4vw;">
                                48
                            </span>
                        </h2>
                    </div>
                
                    <div style="text-align:center; background: rgba(255, 166, 0, 0.20); padding:2px;">
                       <h5 style="color:teal;">Promedio<br> de puntos:</h5>
                        <h2>
                            <span style="color:orange; font-size:4vw;">
                                {round(1935/48, 2)}
                            </span>
                        </h2>
                    </div>
                    
                    <div style="text-align:center; background: rgba(255, 99, 71, 0.20); padding:2px;">
                        <h5 style="color:teal;">Tiempo por<br>vehículo</h5>
                        <h2>
                            <span style="color:tomato; font-size:4vw;">
                                30 min
                            </span>
                        </h2>
                    </div>
                </section>''')
    
# Dashboard
st.subheader(":bar_chart: Dashboard: Cajones azules por barrio")
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
    labels={"count": "", "color": "Barra"},
    template="plotly",
)

st.plotly_chart(grafico, use_container_width=True)


st.sidebar.markdown("""
                    ### Contenido
                    
                    - Mapa interactivo con los puntos (cajones azules) totales.
                    - Algunos números al respecto
                    - Dashboard interactivo
                    
                    ###### En el dashboard interactivo, puedes seleccionar y quitar localidades.  \
                            Así mismo, en el mapa interactivo puedes ver los puntos agrupados y desagruparlos al hacer zoom  o clickear sobre ellos.
                    """)