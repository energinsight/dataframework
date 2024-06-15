import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.entsoe import EntsoeLoad
import streamlit as st
from plotly import express as px

from src.utils import createDataFrame
from src.UIutils import load_data


def demand_page(start, end):
    figures = []
    

    # Code for page 1 goes here
    Demand = EntsoeLoad(start, end)
    
    # Load the data
    Dem = load_data(Demand, ['DE_LU', 'FR', 'ES', 'NO_1'])
    Dem_monthly = Dem.resample('M').mean()


    st.title('Actual Load')

    # Display a data table
    #st.write(SpotPrice)

    selected_index = st.slider(
        'Select a date',
        min_value=0,
        max_value=len(Dem.index) - 1,
        value=0
)

    # Filter the data based on the selected date
    selected_date = Dem.index[selected_index]
    filtered_data = Dem[Dem.index >= selected_date]

    filtered_data = filtered_data.dropna()
    figpr = px.line(filtered_data, x=filtered_data.index, y=filtered_data.columns)
    
    figures.append(figpr)
    
    # Create a plot for the monthly data
    fig_monthly = px.line(Dem_monthly, x=Dem_monthly.index, y=Dem_monthly.columns)
    figures.append(fig_monthly)
    
    for fig in figures:
        st.plotly_chart(fig)

    st.button("Rerun")


