import pandas as pd

from src.entsoe import *
from src.jao import *
from src.utils import createDataFrame


#start = pd.Timestamp('20240605', tz='Europe/Brussels')
start = pd.Timestamp('2024-06-02 22:00:00', tz='Europe/Brussels')
#end = pd.Timestamp('20240606', tz='Europe/Brussels')
end = pd.Timestamp('2024-06-02 23:00:00', tz='Europe/Brussels')

entsopr = EntsoeSpotPrice(start, end)
entsoLoad = EntsoeLoad(start, end)
entsoLoadfcs = EntsoeLoadForecast(start, end)
entsoGenfcs = EntsoeGenerationForecast(start, end)
entsoWindfcs = EntsoeWindForecast(start, end)
entsoSchExchange = EntsoescheduleExchange(start, end)
jaoID2FinalNTC = JaoID2FinalNTC(start, end)
DSfinalcomputation = JaoDAfinalcomputation(start, end)

id2finalNTC = jaoID2FinalNTC.load_data()


DAfinalcomp = DSfinalcomputation.load_data()


DAfinalcompptdf = DAfinalcomp[['ptdf_ALBE', 'ptdf_ALDE', 'ptdf_AT',
       'ptdf_BE', 'ptdf_CZ', 'ptdf_DE', 'ptdf_FR', 'ptdf_HR', 'ptdf_HU',
       'ptdf_NL', 'ptdf_PL', 'ptdf_RO', 'ptdf_SI', 'ptdf_SK']]

id2finalNTC = jaoID2FinalNTC.load_data()

SpotPrice = createDataFrame(entsopr, ['DE_LU', 'FR'])
load = createDataFrame(entsoLoad, ['DE_LU', 'FR'])
LoadForecast = createDataFrame(entsoLoadfcs, ['DE_LU', 'FR'])
#GenForecast = createDataFrame(entsoGenfcs, ['DE_LU', 'FR'])
WindForecast = createDataFrame(entsoWindfcs, ['DE_LU', 'FR'])
Exchanges = createDataFrame(entsoSchExchange, [('DE_LU', 'FR'),('FR','DE_LU')])

