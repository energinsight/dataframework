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

    def load_data(self, country_code):

        # methods that return Pandas Series
        data = self.client.query_day_ahead_prices(country_code, start=self.start, end=self.end)
        
        return data
    
class EntsoeLoad(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, country_code):

        # methods that return Pandas Series
        data = self.client.query_load(country_code, start=self.start, end=self.end)
        
        return data



class EntsoeLoadForecast(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, country_code):

        # methods that return Pandas Series
        data = self.client.query_load_forecast(country_code, start=self.start, end=self.end)
        
        return data

class EntsoeGenerationForecast(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, country_code):

        # methods that return Pandas Series
        data = self.client.query_generation_forecast(country_code, start=self.start, end=self.end)
        
        return data
    
class EntsoeWindForecast(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, country_code):

        # methods that return Pandas Series
        data = self.client.query_wind_and_solar_forecast(country_code, start=self.start, end=self.end)
        
        return data
    
class EntsoescheduleExchange(ENTSOEDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, country_code_from_to):
        
        # methods that return Pandas Series
        country_code_from = country_code_from_to[0]
        country_code_to = country_code_from_to[1]
        data = self.client.query_scheduled_exchanges(country_code_from, country_code_to, start=self.start, end=self.end, dayahead=True)
        
        return data
