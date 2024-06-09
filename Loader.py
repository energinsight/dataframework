import pandas as pd

from src.entsoe import *
#EntsoeSpotPrice, EntsoeLoad, EntsoeLoadForecast, EntsoescheduleExchange
from src.jao import JaoID2FinalNTC
from src.utils import load_data_from_source, createDataFrame
from src.DataStructuring import structure
from src.parameters import params

start = pd.Timestamp('20240609', tz='Europe/Brussels')
end = pd.Timestamp('20240610', tz='Europe/Brussels')


entsopr = EntsoeSpotPrice(start, end)
entsoLoad = EntsoeLoad(start, end)
entsoLoadfcs = EntsoeLoadForecast(start, end)
entsoGenfcs = EntsoeGenerationForecast(start, end)
entsoWindfcs = EntsoeWindForecast(start, end)
entsoSchExchange = EntsoescheduleExchange(start, end)
jao = JaoID2FinalNTC(start, end)

SpotPrice = createDataFrame(entsopr, ['DE_LU', 'FR'])
load = createDataFrame(entsoLoad, ['DE_LU', 'FR'])
LoadForecast = createDataFrame(entsoLoadfcs, ['DE_LU', 'FR'])
#GenForecast = createDataFrame(entsoGenfcs, ['DE_LU', 'FR'])
WindForecast = createDataFrame(entsoWindfcs, ['DE_LU', 'FR'])
Exchanges = createDataFrame(entsoSchExchange, [('DE_LU', 'FR'),('FR','DE_LU')])












#cdf = structure()


#params = {'country_code': ['DE_LU', 'FR']}


#cdf.createDataFrame(entsopr,params)


# Load data from a Entsoe
#print()

#print(load_data_from_source(entsopr, params))
#print(load_data_from_source(entsoLoad, params))
#print(load_data_from_source(entsoLoadfcs, params))

# Load data from a Jao
#print(load_data_from_source(jao, ''))
# streamlit run main.py
