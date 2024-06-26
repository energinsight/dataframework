import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.entsoe import EntsoeGenerationForecast
import streamlit as st
from plotly import express as px

from src.utils import createDataFrame



@st.cache_data
def load_data(_Loaderobj):
    # Replace this with the code to load your data
    return createDataFrame(_Loaderobj, ['DE_LU', 'FR', 'ES', 'NO_1'])

def Production_page(start, end):

    # Code for page 1 goes here
    GenFCS = EntsoeGenerationForecast(start, end)
    
    # Load the data
    Gen = load_data(GenFCS)
    #SpotPrice = createDataFrame(entsopr, ['DE_LU', 'FR', 'ES', 'NO_1'])

    st.title('Forecasted Generation')

    # Display a data table
    #st.write(SpotPrice)

    selected_index = st.slider(
        'Select a date',
        min_value=0,
        max_value=len(Gen.index) - 1,
        value=0
)

    # Filter the data based on the selected date
    selected_date = Gen.index[selected_index]
    filtered_data = Gen[Gen.index >= selected_date]

    filtered_data = filtered_data.dropna()
    figpr = px.line(filtered_data, x=filtered_data.index, y=filtered_data.columns)
    st.plotly_chart(figpr)

    st.button("Rerun")


