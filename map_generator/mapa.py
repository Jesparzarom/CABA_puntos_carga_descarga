import pandas as pd
import folium
from folium.plugins import MarkerCluster

def data_frame():
    #   Creación del Data Frame a partir de un archivo csv
    documento = "datasets\cajones-para-carga-y-descarga.xlsx"
    dataset = pd.read_excel(documento)
    return dataset


dataset = data_frame()


def mapa(dataset=data_frame(), caba=[-34.59, -58.38]):
    #   Variables
    caba = [-34.59, -58.38]
    mapstyle = "OpenStreetMap"
    zoom = 10

    #   Creando mapa
    m = folium.Map(location=caba, zoom_start=zoom, tiles=mapstyle, prefer_canvas=True)
    clusters = MarkerCluster(overlay=True, control=True)

    '''
    #   Agregando un menú y tipos de mapa
    tiles = [folium.TileLayer("OpenStreetMap"), folium.TileLayer("Stamen Terrain")]
    [clusters.add_child(tile) for tile in tiles]
    '''

    #   Agregando marcadores y popup's en cada punto (tupla de coordenadas)
    for ubicacion, pop in zip(
        (dataset[["lat", "long"]].values), (dataset["direccion"].values)
    ):

        #   Marcadores (clusters childs)
        clusters.add_child(
            folium.Marker(
                location=tuple(ubicacion),
                popup=folium.Popup(pop, parse_html=True),
                icon=folium.Icon(color="darkblue", icon="truck", angle=0, prefix="fa"),
            )
        )


    ''' #   Circulos 
        clusters.add_child(
            folium.CircleMarker(
                location=tuple(ubicacion),
                color="purple",
                fill_color="darkpurple",
                radius="5",
                fill_opacity=0.2,
            )
        )
    '''
    #   Agregando Clusters al mapa
    m.add_child(clusters)

    #   Guardar/crear mapa en formato HTML
    template = "Templates\mapa.html"
    #   m.save(template)
    return m.save(template)


#mapa(dataset)