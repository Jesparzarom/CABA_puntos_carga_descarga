# [PUNTOS DE CARGA Y DESCARGA][1]

<hr>

#### Proyecto de mapeo y tratamiento de datos del dataset de puntos de carga y descarga habilitados en la Ciudad Autónoma de Buenos Aires. 

## Los objetivos del proyecto fueron:
-> Visualización de un mapa interactivo de los puntos en general,   
-> Visualización un mapa interactivo de los puntos filtrando la visualización por barrio,  
-> Graficación de un dashboard que permita observar cómo se encuentran distribuidos los puntos,  
-> Incluir algunos datos relevantes.  
-> Deployar los mapas, gráficos y datos en una WebApp con streamlit.  

---

## [streamlit][st] (WebApp)
###  Se usó la librería de streamlit para crear la app web. Así mismo, se utilizó el servicio de [Streamlit Cloud][2] para deployar la misma. Además de streamlit, las librerías utilizadas para los distintos objetivos fueron:

### [Pandas][pd] (Data frames)
- Se importó en formato .xlsxa un data frame para posteriormente manipularlo. Las modificaciones hechas al dataset original constaron de eliminación de las columnas `["calle_nombre", "calle_altura", "codigo_postal_argentino", "codigo_postal"]` y corrección de los campos del dataset  con valores _NaN_ por _"Sin dato"_ excepto las columnas de _"long" y "lat"_. La razón para no eliminarlos por completo las filas que contenían estos valores, yace en el hecho de que proveen ubicaciones mas allá de estár sin identificar. La corrección se hizo sobre los campos del barrio Nuñez, identificado de forma ilegible como "Nu\u00f1ez". Se conservaron las columnas `["lat", "long", "dirección", "comunas"]`

- Se agrupó por _"barrio"_ y se creo un nuevo dataset con las columnas `["lat", "long", "comunas"]`,  posteriormente se agregaron nuevas columnas: `"puntos_totales"` (los puntos sumados y agrupados por barrio) y `"%"`(porcentaje de puntos por barrio sobre el total)

### [Folium][folium] (Mapas)
- Se usaron como parametros de creación de mapa la ubicación CABA, estilo de mapa "Open Street Maps" y zoom x10.
- Los puntos se establecieron con las columnas _"lat" y "long"_, las cuales tienen las coordenadas de los puntos de carga y descarga. de igual forma los _popup's_ se definieron con la columna _"direccion"_

### [Plotly-express][plx] (Gráficos)
- Con el dataset modificado se crearon los gráficos:
    - Bar (Puntos totales)
    - Scatter (Porcentajes)
    - Treemap (Integral)



[1]:https://puntos-carga-descarga-caba.streamlitapp.com/
[2]:https://streamlit.io/cloud
[st]:https://streamlit.io/
[pd]:https://pandas.pydata.org/
[folium]:https://python-visualization.github.io/folium/
[plx]:https://plotly.com/python/

---

<p align="center"><b>Autor:<b> J. Esparza Romero.<br><b>Powered by Python<b></p>