import folium
from haversine import haversine

departureLocation = [38.307339, 127.251953]

targetLocationList = list()
targetLocationList.append([38.257339, 127.251953])
targetLocationList.append([38.307339, 127.261953])
targetLocationList.append([38.297339, 127.271953])

kmap = folium.Map(location=departureLocation, zoom_start=10)

folium.Marker(departureLocation, popup='start', icon=folium.Icon(color='blue',icon='star')).add_to(kmap)

for i in range(len(targetLocationList)):
    dist = haversine(departureLocation, targetLocationList[i])
    dist = round(dist, 4)
    res = str(dist)
    res += 'KM'
    folium.Marker(targetLocationList[i], popup=res, icon=folium.Icon(color='red',icon='star')).add_to(kmap)

kmap.save('map.html')