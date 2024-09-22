import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Try Your Hand At WKT!')
st.write('WKT means Well-Known Text and represents vector geometry in an easy to understand format. Below are some samples of WKT to try!')

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



