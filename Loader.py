import pandas as pd

from src.entsoe import EntsoeSpotPrice, EntsoeLoad, EntsoeLoadForecast
from src.jao import JaoID2FinalNTC
from src.utils import load_data_from_source

start = pd.Timestamp('20240603', tz='Europe/Brussels')
end = pd.Timestamp('20240604', tz='Europe/Brussels')


entsopr = EntsoeSpotPrice()
entsoLoad = EntsoeLoad()
entsoLoadfcs = EntsoeLoadForecast()

jao = JaoID2FinalNTC(start, end)



params = {'start': start,
          'end': end,
          'country_code': 'DE_LU'}


# Load data from a Entsoe
print(load_data_from_source(entsopr, params))
print(load_data_from_source(entsoLoad, params))
print(load_data_from_source(entsoLoadfcs, params))

# Load data from a Jao
print(load_data_from_source(jao, ''))
# streamlit run main.py
