import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09],zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanos")
#for coordinates in [[38.2,-99.01],[37.2,-98.01]]:
for lt, ln, el in zip(lat, lon, elev):   #zip function distributes itemst 1 by 1 from the 2 lists
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m",
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))
#if blank page from popup with "", use -- popup=folium.Popup(str(el),parse_html=True)

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <+ x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("/Map-of-USA-volcanos/Map1.html")
