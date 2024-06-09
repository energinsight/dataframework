import pandas as pd

from src.entsoe import *
from src.jao import *
from src.utils import createDataFrame


start = pd.Timestamp('20240605', tz='Europe/Brussels')
end = pd.Timestamp('20240606', tz='Europe/Brussels')


entsopr = EntsoeSpotPrice(start, end)
entsoLoad = EntsoeLoad(start, end)
entsoLoadfcs = EntsoeLoadForecast(start, end)
entsoGenfcs = EntsoeGenerationForecast(start, end)
entsoWindfcs = EntsoeWindForecast(start, end)
entsoSchExchange = EntsoescheduleExchange(start, end)
jaoID2FinalNTC = JaoID2FinalNTC(start, end)

id2finalNTC = jaoID2FinalNTC.load_data()

SpotPrice = createDataFrame(entsopr, ['DE_LU', 'FR'])
load = createDataFrame(entsoLoad, ['DE_LU', 'FR'])
LoadForecast = createDataFrame(entsoLoadfcs, ['DE_LU', 'FR'])
#GenForecast = createDataFrame(entsoGenfcs, ['DE_LU', 'FR'])
WindForecast = createDataFrame(entsoWindfcs, ['DE_LU', 'FR'])
Exchanges = createDataFrame(entsoSchExchange, [('DE_LU', 'FR'),('FR','DE_LU')])

