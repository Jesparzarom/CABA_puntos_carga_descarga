import streamlit as st
from map_generator.mapa import data_frame
from Inicio import grafic_hoods


dataset = data_frame()

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
            El dataset original con el que se trabaj贸, fue recuperado
            desde [BA Data](https://data.buenosaires.gob.ar/dataset/cajones-para-carga-descarga).
             
            Puedes explorarlo aca 馃憞:
            
            
            """
)

st.dataframe(dataset)

st.sidebar.markdown("# :information_source: Informaci贸n")

st.sidebar.markdown('''
                    Informaci贸n sobre el dataset y su origen.
                    
                    ### M贸dulos
                    Los m贸dulos usados para trabajar los datos 
                    en python fueron:
                    - Pandas (DataFrame)
                    - Pyplot-express (Gr谩ficos)
                    - Streamlit (WebApp)
                    
                    ###### Autor: J. Esparza
                    ''')