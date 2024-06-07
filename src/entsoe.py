from.loadertypes import DataLoader
from entsoe import EntsoePandasClient
import os
import pandas as pd

class ENTSOEDataLoader(DataLoader):
    def __init__(self):
        api_key = os.getenv('ENTSOE_API_KEY')
        if not api_key:
            raise ValueError("Missing environment variable: ENTSOE_API_KEY")
        self.client = EntsoePandasClient(api_key=os.getenv('ENTSOE_API_KEY'))

    def load_data(self, params):
        # Load data from ENTSOE
        pass
        #return data
    
class EntsoeSpotPrice(ENTSOEDataLoader):
    def load_data(self, params):
        
        data = super().__init__()
        start = params['start']
        end = params['end']
        country_code = params['country_code'] 

        # methods that return Pandas Series
        data = self.client.query_day_ahead_prices(country_code, start=start, end=end)
        
        return data
    
class EntsoeLoad(ENTSOEDataLoader):
    def load_data(self, params):
        
        data = super().__init__()
        start = params['start']
        end = params['end']
        country_code = params['country_code'] 

        # methods that return Pandas Series
        data = self.client.query_load(country_code, start=start, end=end)
        
        return data



class EntsoeLoadForecast(ENTSOEDataLoader):
    def load_data(self, params):
        
        data = super().__init__()
        start = params['start']
        end = params['end']
        country_code = params['country_code'] 

        # methods that return Pandas Series
        data = self.client.query_load_forecast(country_code, start=start, end=end)
        
        return data

class EntsoeGenerationForecast(ENTSOEDataLoader):
    def load_data(self, params):
        
        data = super().__init__()
        start = params['start']
        end = params['end']
        country_code = params['country_code'] 

        # methods that return Pandas Series
        data = self.client.query_generation_forecast(country_code, start=start, end=end)
        
        return data