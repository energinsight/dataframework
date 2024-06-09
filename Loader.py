import pandas as pd
import streamlit as st
import plotly.express as px

from src.entsoe import *
from src.jao import *
from src.utils import createDataFrame


#start = pd.Timestamp('20240605', tz='Europe/Brussels')
start = pd.Timestamp('2024-06-01 00:00:00', tz='Europe/Brussels')
#end = pd.Timestamp('20240606', tz='Europe/Brussels')
end = pd.Timestamp('2024-06-09 23:00:00', tz='Europe/Brussels')

entsopr = EntsoeSpotPrice(start, end)
entsoLoad = EntsoeLoad(start, end)
entsoLoadfcs = EntsoeLoadForecast(start, end)
entsoGenfcs = EntsoeGenerationForecast(start, end)
entsoWindfcs = EntsoeWindForecast(start, end)
entsoSchExchange = EntsoescheduleExchange(start, end)
jaoID2FinalNTC = JaoID2FinalNTC(start, end)
DSfinalcomputation = JaoDAfinalcomputation(start, end)

id2finalNTC = jaoID2FinalNTC.load_data()


#DAfinalcomp = DSfinalcomputation.load_data()


#DAfinalcompptdf = DAfinalcomp[['ptdf_ALBE', 'ptdf_ALDE', 'ptdf_AT',
#       'ptdf_BE', 'ptdf_CZ', 'ptdf_DE', 'ptdf_FR', 'ptdf_HR', 'ptdf_HU',
#       'ptdf_NL', 'ptdf_PL', 'ptdf_RO', 'ptdf_SI', 'ptdf_SK']]

id2finalNTC = jaoID2FinalNTC.load_data()

SpotPrice = createDataFrame(entsopr, ['DE_LU', 'FR', 'ES'])
load = createDataFrame(entsoLoad, ['DE_LU', 'FR'])
LoadForecast = createDataFrame(entsoLoadfcs, ['DE_LU', 'FR'])
#GenForecast = createDataFrame(entsoGenfcs, ['DE_LU', 'FR'])
WindForecast = createDataFrame(entsoWindfcs, ['DE_LU', 'FR'])
Exchanges = createDataFrame(entsoSchExchange, [('DE_LU', 'FR'),('FR','DE_LU')])

# Display a header
st.title('My Streamlit App')

# Display a data table
st.write(SpotPrice)

selected_index = st.slider(
    'Select a date',
    min_value=0,
    max_value=len(SpotPrice.index) - 1,
    value=0
)

# Get the selected date from the index
selected_date = SpotPrice.index[selected_index]

# Filter the DataFrame based on the selected date
filtered_data = SpotPrice[SpotPrice.index >= selected_date]

figpr = px.line(filtered_data, x=filtered_data.index, y=filtered_data.columns)
st.plotly_chart(figpr)

figRes = px.line(WindForecast, x=WindForecast.index, y=WindForecast.columns)
st.plotly_chart(figRes)

figload = px.line(load, x=load.index, y=load.columns)
st.plotly_chart(figload)

figLoadForecast = px.line(LoadForecast, x=LoadForecast.index, y=LoadForecast.columns)
st.plotly_chart(figLoadForecast)