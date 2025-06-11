import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

# Set page to take up whole screen
st.set_page_config(layout="wide")

# Header
st.write("""
# Analysis of Public Debt under Presidents
""")

# Spreadsheet to DataFrame
df = pd.read_excel('federaldebt_pres.xlsx')

# First selectbox sets data range for second select slider
selection = st.selectbox(
    "Option 1. Select a President",
    options = df['president'].drop_duplicates()
)

# Creates a range tuple used in Dataframe creation for graphs
selection1 = df[df['president']==selection]
min_val1 = selection1['date'].min()
max_val1 = selection1['date'].max()
range_val = (min_val1,max_val1)

# Second selection adjusts date range
start1, stop1 = st.select_slider(
    "Option 2. Select a date range",
    options=df['date'].to_list(),
    value=range_val
    )

# Second selection creates start and stop point for new Dataframe for charts
start = df[df['date']==start1].index[0]
stop = df[df['date']==stop1].index[0]
new_df = df[start:stop]

col1, col2, col3 = st.columns(3)

with col1:
    # Create bar chart with different colors for each president
    fig1 = px.bar(new_df, x='date', y='ratio', color='president',
                  labels={
                         "date": "Date",
                         "ratio": "Debt/GDP"
                     },
                    title="Federal Debt as % of GDP")
    
    # Style chart
    fig1.update_yaxes(
        showline=True, linewidth=2, linecolor='white', gridcolor='white', gridwidth=0.5)
    fig1.update_xaxes(
        showline=True, linewidth=2, linecolor='white')
    fig1.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)'
    )
    st.plotly_chart(fig1, theme=None)

with col2:
    # Create bar chart with different colors for each president
    fig2 = px.bar(new_df, x='date', y='deficit', color='president',
                  labels={
                         "date": "Date",
                         "deficit": "Surplus or Deficit/GDP"
                     },
                    title="Federal Surplus or Deficit as % of GDP")
    
    # Style chart
    fig2.update_yaxes(
        showline=True, linewidth=2, linecolor='white', gridcolor='white', gridwidth=0.5)
    fig2.update_xaxes(
        showline=True, linewidth=2, linecolor='white')
    fig2.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)'
    )
    st.plotly_chart(fig2, theme=None)

with col3:
    # Create pie chart
    fig3 = px.pie(new_df, values='count', names='president', title="Democrat-Republican % of Selection", color='color')
    fig3.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig3, theme=None)



# Footer
st.write('Created by Andrew French')
st.write('main data source: U.S. Office of Management and Budget and Federal Reserve Bank of St. Louis')





