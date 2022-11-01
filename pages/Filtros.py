from Inicio import st, components, seleccion, dataset2
from map_generator.mapa import mapa


# ----- START STREAMLIT -----
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

# ---- SIDEBAR ----
st.sidebar.markdown("# :mag_right: Datos Filtrados")
st.sidebar.write(''' En esta página puedes interactuar
                 un poco con los datos. ''')

# Desplegamos un menu de opciones con los nombres de los barrios, únicos, en el sidebar, 
# a modo de filtro para usar sus valores en el mapa, y en los datos númericos informativos. 
Barrio = st.sidebar.selectbox("Selecciona un barrrio",
                                options=dataset2["barrio"].unique(),
                                index=3,)

# Guardamos los valores de la selección de la variable Barrio.
seleccion = dataset2.query("barrio == @Barrio")
st.sidebar.markdown('''##### Una vez seleccionado un barrio de CABA, veras los cambios reflejados en el mapa''')
st.sidebar.markdown('''
                 ''')
             
                        
# --- FILTROS PAGE ---
st.subheader(":pushpin: Mapa interactivo")

# Esto devuelve valores únicos, tanto de barrios, como una ubicación promedio de los puntos 
# por barrio. Se asignan los valores a una lista, para una manipulación más flexible.
grupos = dataset2.groupby(["barrio"])["lat", "long"].mean()
grupos = grupos.values.tolist()

# Mostrando el mapa en la pantalla
if seleccion["barrio"].count() != 1935:
    mapa(seleccion, grupos)
    p = open("./Templates/mapa.html")
    components.html(p.read(), height=400)

# Acciones condicionales sobre los datos informativos
if seleccion["barrio"].count() != 1935:
    components.html(f'''
                    <section style="display:flex; justify-content:space-around; background: #06648C; 
                    text-shadow:1px 1px 10px rgba(0, 0, 0, 0.50); font-family:Lucida Grande;">
                        <div style="text-align:center;">
                            <h4 style="color:white;">Localidad</h4>   
                            <h2>
                                <span style="color:orange;">
                                    {Barrio}
                                </span>
                            </h2>
                        </div>
                        <div style="text-align:center;">
                            <h4 style="color:white;">Cajones</h4>
                            <h2>
                                <span style="color:tomato; font-size:30px;">
                                    {(seleccion["barrio"].count())}
                                </span>
                            </h2>
                        </div>
                    </section>''')

st.sidebar.markdown("""
##### Espacio de carga y descarga (Cajón Azul) 
>  Son un espacio físico delimitado destinado exclusivamente a dicha actividad. \
Deben ser utilizados por todos los comercios de cercanía.


> El tiempo máximo de permanencia es de 30 minutos, excepto que la cartelería indique otro tiempo.

> Los vehículos que realicen la operación de carga y descarga deberán manteniener las luces balizas intermitentes encendidas.
            """)

st.markdown("""
            ### Observaciones:
            - En las opciones del menú de barrios, la etiqueta "Sin datos" fue para reemplazar celdas vacías(NaN) en el dataset. \
              Sin embargo, es curioso notar que los puntos están distribuidos al rededor de toda la Avenida Rivadavia, desde Liniers \
              hasta San Nicolás.
              
            - Algunos errores ortográficos en los nombres de los barrios de CABA, fueron heredados del dataset. \
              Por practicidad se dejarón ya que el objetivo principal fue mostrarlos en un mapa interactivo.      \
              **Puedes ver los datos sin modificacion en la pestaña de "Info"** """)