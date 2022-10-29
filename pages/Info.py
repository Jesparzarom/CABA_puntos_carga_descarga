import streamlit as st
from map_generator.mapa import dataset


st.set_page_config(
    page_title="Puntos de Carga y Descarga en CABA",
    page_icon=":truck:",
    layout="centered",
    menu_items={
        "Get Help": "https://github.com/Jesparzarom/CABA_puntos_carga_descarga",
        "Report a bug": "https://github.com/Jesparzarom/CABA_puntos_carga_descarga",
        "About": "## Powered by Python.:snake: ```Autor: J. Esparza R.``` ",
    },
)

st.markdown(
    """
            ## Informacion
            El dataset original con el que se trabajó, fue recuperado
            desde [BA Data](https://data.buenosaires.gob.ar/dataset/cajones-para-carga-descarga).
             
            Puedes explorarlo aca 👇:
            
            
            """
)

st.dataframe(dataset)

st.sidebar.markdown("# :information_source: Información")

st.sidebar.markdown('''
                    Información sobre el dataset y su origen.
                    
                    ### Módulos
                    Los módulos usados para trabajar los datos 
                    en python fueron:
                    - Pandas (DataFrame)
                    - Pyplot-express (Gráficos)
                    - Streamlit (WebApp)
                    
                    ###### Autor: J. Esparza
                    ''')