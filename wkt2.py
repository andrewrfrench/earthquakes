import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Try Your Hand At WKT!')
st.write('WKT means Well-Known Text and represents vector geometry in an easy to understand format.  Below are some samples of WKT to try!')

st.write("""POINT (30 10)  
	LINESTRING (30 10, 10 30, 40 40)  
	POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))  
	POLYGON ((35 10, 45 45, 15 40, 10 20, 35 10),  
	(20 30, 35 35, 30 20, 20 30))""")

user = st.text_input("Enter WKT Below", value='POLYGON ((40 40, 20 45, 45 30, 40 40))')

entry = user
st.write("This is what you wrote:", entry)
wkts = [
entry
]

s = gpd.GeoSeries.from_wkt(wkts)
y =gpd.GeoDataFrame(s)

fig, axes = plt.subplots()

s.plot(ax=axes)

st.pyplot(fig)



