from.loaderAPI import DataLoader
from entsoe import EntsoePandasClient
import os
import pandas as pd

class ENTSOEDataLoader(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)
        api_key = os.getenv('ENTSOE_API_KEY')
        if not api_key:
            raise ValueError("Missing environment variable: ENTSOE_API_KEY")
        self.client = EntsoePandasClient(api_key=os.getenv('ENTSOE_API_KEY'))

    def load_data(self, params):
        # Load data from ENTSOE
        pass
        #return data
    
class EntsoeSpotPrice(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, params):

        country_code = params['country_code'] 

        # methods that return Pandas Series
        data = self.client.query_day_ahead_prices(country_code, start=self.start, end=self.end)
        
        return data
    
class EntsoeLoad(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, params):
        
        country_code = params['country_code'] 

        # methods that return Pandas Series
        data = self.client.query_load(country_code, start=self.start, end=self.end)
        
        return data



class EntsoeLoadForecast(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, params):
        
        country_code = params['country_code'] 

        # methods that return Pandas Series
        data = self.client.query_load_forecast(country_code, start=self.start, end=self.end)
        
        return data

class EntsoeGenerationForecast(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, params):
        
        country_code = params['country_code'] 

        # methods that return Pandas Series
        data = self.client.query_generation_forecast(country_code, start=self.start, end=self.end)
        
        return data