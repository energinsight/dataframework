import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.entsoe import EntsoeLoad
import streamlit as st
from plotly import express as px

from src.utils import createDataFrame


@st.cache_data
def load_data(_Loaderobj):
    # Replace this with the code to load your data
    return createDataFrame(_Loaderobj, ['DE_LU', 'FR', 'ES', 'NO_1'])

def demand_page():
    #start = pd.Timestamp('20240605', tz='Europe/Brussels')
    start = pd.Timestamp('2024-05-01 00:00:00', tz='Europe/Brussels')
    #end = pd.Timestamp('20240606', tz='Europe/Brussels')
    end = pd.Timestamp('2024-06-09 23:00:00', tz='Europe/Brussels')

    # Code for page 1 goes here
    Demand = EntsoeLoad(start, end)
    
    # Load the data
    Dem = load_data(Demand)
    #SpotPrice = createDataFrame(entsopr, ['DE_LU', 'FR', 'ES', 'NO_1'])

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
    #figpr = create_plot(filtered_data)
    st.plotly_chart(figpr)

    st.button("Rerun")


