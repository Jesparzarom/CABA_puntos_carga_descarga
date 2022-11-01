import plotly_express as px
import streamlit as st
import streamlit.components.v1 as components
from map_generator.mapa import pd, data_frame

#  --- DATASET ---
dataset = data_frame()

#   Eliminar columnas
dataset2 = dataset.drop(["calle_nombre", "calle_altura", 
                         "codigo_postal_argentino", "codigo_postal"], axis=1)

#   Cambiar valores "NaN" y "Nu\u00f1ez"
dataset2 = dataset2.fillna("Sin dato") 
dataset2 = dataset2.replace("Nu\\u00f1ez","Nuñez") 

#   Ordenar valores alfabéticamente.
dataset2 = dataset2.sort_values(by=['barrio']) 
seleccion = dataset2.copy()

#   Agrupar los puntos por barrio
seleccion = seleccion.groupby(["barrio"], as_index=False, sort=True)[["lat", "long"]].mean()
seleccion = pd.DataFrame(seleccion)

#   Asignar Variables "puntos_totales" a puntos totales por barrio y coords a lista de coordenadas
puntos_totales = dataset2["barrio"].value_counts(sort=False).values # Puntos totales por barrio
coords = seleccion[["lat", "long"]].values  # Lista de coordenadas

#   Insertar columna de puntos totales en el Data Frame "seleccion" en la columna 0 + 1
seleccion.insert(1, "puntos_totales", puntos_totales)

#   Calcular porcentaje de puntos por barrio sobre el total.
porcentaje = [(str(round((puntos/1935)*100, 2))+"%") for puntos in seleccion["puntos_totales"].values]


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
            <header style="background: #2B2E4A; text-align:center; border-radius:10px;">    
                <h1 style="font-size:4vw; padding:5px; border-radius:10px; color:white;">Puntos de Carga y Descarga en CABA</h1>
            </header> 
            ''')

#   Mapa interactivo (Importado directamente del directorio ./Templates/)
st.subheader(":pushpin: Mapeo interactivo de los puntos")
p = open("./Templates/mapa2.html")
components.html(p.read(), height=300)


components.html(f'''
                <section style="display:flex; background: #2B2E4A; justify-content:space-around; text-shadow:1px 1px 10px rgba(0, 0, 0, 0.50); font-family:Lucida Grande;">
                
                    <div style="text-align:center; padding:2px;">
                        <h5 style="color:#8D9EFF;">Puntos totales<br> en CABA:</h5>
                        <h2>
                            <span style="color:white; font-size:4vw; ">
                                {1935}
                            </span>
                        </h2>
                    </div>
                    
                    <div style="text-align:center; padding:2px; ">
                        <h5 style="color:#8D9EFF;">Barrios en<br> CABA:</h5>
                        <h2>
                            <span style="color:#00C1D4; font-size:4vw;">
                                48
                            </span>
                        </h2>
                    </div>
                
                    <div style="text-align:center; padding:2px;">
                       <h5 style="color:#8D9EFF;">Promedio<br> de puntos:</h5>
                        <h2>
                            <span style="color:orange; font-size:4vw;">
                                {round(1935/48, 2)}
                            </span>
                        </h2>
                    </div>
                    
                    <div style="text-align:center; padding:2px;">
                        <h5 style="color:#8D9EFF;">Tiempo por<br>vehículo</h5>
                        <h2>
                            <span style="color:#F8485E; font-size:4vw;">
                                30 min
                            </span>
                        </h2>
                    </div>
                </section>''')

# --- DASHBOARD ---
st.subheader(":bar_chart: Dashboard: Cajones azules por barrio")
grafic_hoods = seleccion

grafico = px.bar(
    grafic_hoods,
    color=grafic_hoods["puntos_totales"],
    y="barrio",
    x="puntos_totales",
    orientation="h",
    width=500,
    height=800,
    template="plotly",
)
st.plotly_chart(grafico, use_container_width=True)

st.sidebar.markdown("""
                    ### Contenido
                    
                   - Mapa interactivo con los puntos (cajones azules) totales.
                   - Algunos números al respecto
                   - Dashboard interactivo
                    
                    ###### En el dashboard interactivo, puedes seleccionar y quitar localidades.  \
                           Así mismo, en el mapa interactivo puedes ver los puntos agrupados y desagruparlos \ 
                           al hacer zoom  o clickear sobre ellos.
                    """)

st.write("""
         <style>
            .eczokvf1{
                background-image: url(https://cdn.pixabay.com/photo/2016/11/19/18/46/concrete-1840731_960_720.jpg);
                background-repeat:repeat;

                }
        </style>""", 
        unsafe_allow_html=True)