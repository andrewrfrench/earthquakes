import numpy as np
import pandas as pd
import streamlit as st
import requests
from datetime import datetime
       
# Set page to take up whole screen
st.set_page_config(layout="wide")

# Selection to choose between two parameters
selection = st.selectbox('Select One', ('Time', 'Magnitude'))

if selection == 'Time':
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "orderby": "time",
        "limit": 3,
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200: 
        data = response.json()
       
        earthquake1 = data["features"][0]
        earthquake2 = data["features"][1]
        earthquake3 = data["features"][2]
        
        e1_dict = {
                    "code":  earthquake1['properties']['code'],
                    "place": earthquake1['properties']['place'],
                    "magnitude" : earthquake1['properties']["mag"],
                    "timestamp": datetime.fromtimestamp(earthquake1['properties']["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    "longitude": earthquake1["geometry"]["coordinates"][0],
                    "latitude": earthquake1["geometry"]["coordinates"][1]
                   }
        e2_dict = {
                    "code":  earthquake2['properties']['code'],
                    "place": earthquake2['properties']['place'],
                    "magnitude" : earthquake2['properties']["mag"],
                    "timestamp": datetime.fromtimestamp(earthquake2['properties']["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    "longitude": earthquake2["geometry"]["coordinates"][0],
                    "latitude": earthquake2["geometry"]["coordinates"][1]
                   }
        e3_dict = {
                    "code":  earthquake3['properties']['code'],
                    "place": earthquake3['properties']['place'],
                    "magnitude" : earthquake3['properties']["mag"],
                    "timestamp": datetime.fromtimestamp(earthquake3['properties']["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    "longitude": earthquake3["geometry"]["coordinates"][0],
                    "latitude": earthquake3["geometry"]["coordinates"][1]
                   }  
        e1 = pd.DataFrame.from_dict(e1_dict,orient='index').T
        e2 = pd.DataFrame.from_dict(e2_dict,orient='index').T
        e3 = pd.DataFrame.from_dict(e3_dict,orient='index').T
        
        earthquakes = pd.concat([e1,e2,e3]).reset_index(drop=True)
    else:
        f = "failure"
    
    st.title('Most Recent Earthquakes')
    st.text('  ')
    
    row1, row2, row3 = st.columns(3)
    
    container = st.container(border=True)
    
    note = earthquakes['place'][0]
      
    with container:
        with row1:
            st.map(earthquakes[:1], zoom=6, color='#FF0000', size=125)
            st.text('Magnitude:')
            st.text(earthquakes['magnitude'][0])
            st.text('When:' )
            st.text(earthquakes['timestamp'][0])
            st.text("Where:")
            st.text(earthquakes['place'][0])
        with row2:
            st.map(earthquakes[1:2], zoom=6)
            st.text('Magnitude:')
            st.text(earthquakes['magnitude'][1])
            st.text('When:' )
            st.text(earthquakes['timestamp'][1])
            st.text("Where:")
            st.text(earthquakes['place'][1])
        with row3:
            st.map(earthquakes[2:3], zoom=6)
            st.text('Magnitude:')
            st.text(earthquakes['magnitude'][2])
            st.text('When:' )
            st.text(earthquakes['timestamp'][2])
            st.text("Where:")
            st.text(earthquakes['place'][2])
            
elif selection == 'Magnitude':
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "orderby": "magnitude",
        "limit": 3,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200: 
        data = response.json()
       
        earthquake1 = data["features"][0]
        earthquake2 = data["features"][1]
        earthquake3 = data["features"][2]
        
        e1_dict = {
                    "code":  earthquake1['properties']['code'],
                    "place": earthquake1['properties']['place'],
                    "magnitude" : earthquake1['properties']["mag"],
                    "timestamp": datetime.fromtimestamp(earthquake1['properties']["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    "longitude": earthquake1["geometry"]["coordinates"][0],
                    "latitude": earthquake1["geometry"]["coordinates"][1]
                   }
        e2_dict = {
                    "code":  earthquake2['properties']['code'],
                    "place": earthquake2['properties']['place'],
                    "magnitude" : earthquake2['properties']["mag"],
                    "timestamp": datetime.fromtimestamp(earthquake2['properties']["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    "longitude": earthquake2["geometry"]["coordinates"][0],
                    "latitude": earthquake2["geometry"]["coordinates"][1]
                   }
        e3_dict = {
                    "code":  earthquake3['properties']['code'],
                    "place": earthquake3['properties']['place'],
                    "magnitude" : earthquake3['properties']["mag"],
                    "timestamp": datetime.fromtimestamp(earthquake3['properties']["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    "longitude": earthquake3["geometry"]["coordinates"][0],
                    "latitude": earthquake3["geometry"]["coordinates"][1]
                   }  
        e1 = pd.DataFrame.from_dict(e1_dict,orient='index').T
        e2 = pd.DataFrame.from_dict(e2_dict,orient='index').T
        e3 = pd.DataFrame.from_dict(e3_dict,orient='index').T
        
        earthquakes = pd.concat([e1,e2,e3]).reset_index(drop=True)
    else:
        f = "failure"
    
    st.title('Recent High Magnitude Earthquakes')
    st.text('  ')

    
    row1, row2, row3 = st.columns(3)
    
    container = st.container(border=True)
    
    note = earthquakes['place'][0]
      
    with container:
        with row1:
            st.map(earthquakes[:1], zoom=6)
            st.text('Magnitude:')
            st.text(earthquakes['magnitude'][0])
            st.text('When:' )
            st.text(earthquakes['timestamp'][0])
            st.text("Where:")
            st.text(earthquakes['place'][0])
        with row2:
            st.map(earthquakes[1:2], zoom=6)
            st.text('Magnitude:')
            st.text(earthquakes['magnitude'][1])
            st.text('When:' )
            st.text(earthquakes['timestamp'][1])
            st.text("Where:")
            st.text(earthquakes['place'][1])
        with row3:
            st.map(earthquakes[2:3], zoom=6)
            st.text('Magnitude:')
            st.text(earthquakes['magnitude'][2])
            st.text('When:' )
            st.text(earthquakes['timestamp'][2])
            st.text("Where:")
            st.text(earthquakes['place'][2])

st.text('')
st.text('')
st.text('')
st.text('Created by Andrew French')
st.text('data source: USGS')
