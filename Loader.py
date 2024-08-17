import pandas as pd
from plotly import express as px

from src.entsoe import *
from src.jao import *
from src.netztransparenz import *
from src.utils import createDataFrame


start = pd.Timestamp('2024-06-01 00:00:00', tz='Europe/Brussels')
end = pd.Timestamp('2024-06-09 23:00:00', tz='Europe/Brussels')

reBAP1 = reBAP(start, end)

reBAP1.load_data()


entsopr = EntsoeSpotPrice(start, end)
entsoLoad = EntsoeLoad(start, end)
entsoLoadfcs = EntsoeLoadForecast(start, end)
entsoGenfcs = EntsoeGenerationForecast(start, end)
entsoWindfcs = EntsoeWindForecast(start, end)
entsoSchExchange = EntsoescheduleExchange(start, end)
jaoID2FinalNTC = JaoID2FinalNTC(start, end)
DSfinalcomputation = JaoDAfinalcomputation(start, end)


# Load the data
SpotPrice = createDataFrame(entsopr, ['DE_LU', 'FR', 'ES', 'NO_1'])

entsoSchExchange.load_data(['FR','DE_LU'])
jaoID2FinalNTC.load_data()

a=2