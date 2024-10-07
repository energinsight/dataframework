import pandas as pd
from plotly import express as px
'''
from dataframework.entsoe import *
from dataframework.jaoCore import *
from dataframework.jaoCoreID import *
from dataframework.netztransparenz import *
from dataframework.utils import DataFrame_sameloader, DataFrame_vl
from dataframework.entsoeBalancing import *
'''
from dataframework.entsoe_generation import *
from dataframework.entsoeBalancing import BalancingEnergyBids as eng


start = pd.Timestamp('2024-10-05 2:00:00', tz='Europe/Brussels')   # 
end = pd.Timestamp('2024-10-05 3:00:00', tz='Europe/Brussels')


bal = eng(start, end)

ba = bal.load_data("SCA|DE(Amprion)", "Automatic frequency restoration reserve", "Reserve bid document", "Offer")


a = ENTSOEGeneration(start, end)


aa = a.load_data("BZN|DE-LU", 'Generation forecast', 'Day ahead')
bb = a.load_data("BZN|FR", 'Generation forecast', 'Day ahead')


#aa = Imbalance(start, end)
#bb = aa.load_data('10YCZ-CEPS-----N')
'''
shadowProbj = Jaocore_shadowprices(start, end)


shadowProbj = Jaocore_shadowprices(start, end)
aa = shadowProbj.load_data()

finalatcforsidc = IDCCB_initialcomputation(start, end)
rp = finalatcforsidc.load_data()

reBAP1 = reBAP(start, end)

reBAP1.load_data()


entsopr = EntsoeSpotPrice(start, end)
entsoLoad = EntsoeLoad(start, end)
entsoLoadfcs = EntsoeLoadForecast(start, end)
entsoGenfcs = EntsoeGenerationForecast(start, end)
entsoWindfcs = EntsoeWindForecast(start, end)
entsoSchExchange = EntsoescheduleExchange(start, end)

X = DataFrame_vl([entsoLoad,
                     entsoLoadfcs,
                     entsoGenfcs,
                     entsoWindfcs], ['DE_LU', 'DE_LU', 'DE_LU', 'DE_LU'])

# Load the data
SpotPrice = DataFrame_sameloader(entsopr, ['DE_LU', 'FR', 'ES', 'NO_1'])

entsoSchExchange.load_data(['FR','DE_LU'])
'''

