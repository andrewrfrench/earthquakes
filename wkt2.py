import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Try Your Hand At WKT!')
st.write('WKT means Well-Known Text and represents vector geometry in an easy to understand format.')

    
def multi_split(data, delim):
    split1 = data.split(delim)
    new_sp = [item.strip() for item in split1]
    new_l = [f"({x})" for x in new_sp]
    return ' , '.join([str(s) for s in new_l])

with st.sidebar:
    type = st.selectbox('Select one:', ('PRIMITIVES', 'MULTI_PART GEOMETRIES'))
    
    if type == 'PRIMITIVES':
        type2 = st.selectbox('Select one:', ('POINT', 'LINESTRING', 'POLYGON'))
        if type2 == 'POINT':
            coordinate = st.text_input("Enter an X and a Y coordinate:", value='40 50')
            entry = f"{type2} ( {coordinate} )"
        elif type2 == 'LINESTRING':
            coordinate = st.text_input("Enter multiple X and Y coordinates, seperated by commas:", value='40 50, 30 20')
            entry = f"{type2} ( {coordinate} )"
        elif type2 == 'POLYGON':
            coordinate = st.text_input("Enter over three X and Y coordinates, seperated by commas (Polyons must start and stop at same point):", value='40 40, 20 45, 45 30, 40 40')
            entry = f"{type2} (( {coordinate} ))"
        
        
        
    elif type == 'MULTI_PART GEOMETRIES':
        type2 = st.selectbox('Select one:', ('MULTIPOINT', 'MULTILINESTRING', 'MULTIPOLYGON'))
        if type2 == 'MULTIPOINT':
            coordinate = st.text_input("Enter multiple X and a Y coordinate, seperated by commas:", value='40 50, 30 20')
            entry = f"{type2} ( {coordinate} )"
        elif type2 == 'MULTILINESTRING':
            coordinate = st.text_input("Enter multiple X and Y coordinates, seperated by commas, seperate lines by colons:", value='40 50, 30 20 : 100 30, 25 50')
            recalc = multi_split(coordinate, ':')
            entry = f"{type2} ( {recalc} )"
        elif type2 == 'MULTIPOLYGON':
            coordinate = st.text_input("Enter over three X and Y coordinates, seperated by commas, seperate polygons by colons (Polyons must start and stop at same point):", value='40 30, 20 45, 100 50, 40 30 : 100 120, 95 65, 50 55, 100 120')
            recalc = multi_split(coordinate, ':')
            entry = f"{type2} (( {recalc} ))"
    

st.write("This is your WKT output:", entry)

wkts = [
entry
]

s = gpd.GeoSeries.from_wkt(wkts)
y =gpd.GeoDataFrame(s)

plt.style.use('dark_background')
fig, axes = plt.subplots()

s.plot(ax=axes)

st.pyplot(fig)







