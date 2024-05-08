import requests
from bs4 import BeautifulSoup
import pandas as pd
import math
import plotly.express as px
from links import urls
import plotly.graph_objects as go

go.layout.mapbox.AccessToken = "pk.eyJ1IjoibWFja2luYXRvciIsImEiOiJjazJtbHY3ZW4wamM4M2NxZXJvYnJjeDhsIn0.cF5Gsxx6_anrbfMUZg-scA"


def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371
    return c * r

#%%
data = {}
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    if r.status_code != 200:
        continue
    page_data = {}
    div_col_left = soup.find('div', class_='col-left')
    div_col_right = soup.find('div', class_='col-right')
    page_data['name'] = div_col_left.find_all('p')[0].text.split(':')[-1].strip()
    page_data['state'] = div_col_left.find_all('p')[1].text.split(':')[-1].strip()
    page_data['county'] = div_col_left.find_all('p')[2].text.split(':')[-1].strip()
    page_data['elevation'] = div_col_right.find_all('p')[0].text.split(':')[-1].strip()
    page_data['commodity'] = div_col_right.find_all('p')[1].text.split(':')[-1].strip()
    coords = div_col_right.find_all('p')[2].text.split(':')[-1].strip()
    page_data['lat'] = float(coords.split(',')[0].strip())
    page_data['lon'] = float(coords.split(',')[1].strip())
    page_data['distance_km'] = haversine(36.05012744582646, -115.13144470426091 , float(page_data['lat']), float(page_data['lon']))
    data[url] = page_data

df =pd.DataFrame.from_dict(data, orient='index')
df.reset_index(inplace=True)
#%%
fig = px.scatter_mapbox(df, 
                        lat="lat", 
                        lon="lon", 
                        hover_name="name",
                        color="copper",
                        zoom=3,
                        hover_data=["state", "county", "elevation", "commodity", "distance_km"],)
fig.update_layout(mapbox_style="open-street-map")
fig.show()

# %%
