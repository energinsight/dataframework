import pandas as pd
from plotly import express as px

from src.entsoe import *
from src.jao import *
from src.utils import createDataFrame


#start = pd.Timestamp('20240605', tz='Europe/Brussels')
start = pd.Timestamp('2024-06-01 00:00:00', tz='Europe/Brussels')
#end = pd.Timestamp('20240606', tz='Europe/Brussels')
end = pd.Timestamp('2024-06-09 23:00:00', tz='Europe/Brussels')


#alancingEnergyBid = EntsoeBalancingEnergyBid(start, end)
#alancingEnergyBid.load_data('10YDE-VE-------2')

entsopr = EntsoeSpotPrice(start, end)
entsoLoad = EntsoeLoad(start, end)
entsoLoadfcs = EntsoeLoadForecast(start, end)
entsoGenfcs = EntsoeGenerationForecast(start, end)
entsoWindfcs = EntsoeWindForecast(start, end)
entsoSchExchange = EntsoescheduleExchange(start, end)
jaoID2FinalNTC = JaoID2FinalNTC(start, end)
DSfinalcomputation = JaoDAfinalcomputation(start, end)


def load_data():
    # Replace this with the code to load your data
    return createDataFrame(entsopr, ['DE_LU', 'FR', 'ES', 'NO_1'])


# Load the data
SpotPrice = load_data()

a=2