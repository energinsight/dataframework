from.loaderAPI import DataLoader
from entsoe import EntsoePandasClient
import os
import pandas as pd


class ENTSOEBalancingLoader(DataLoader):
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


class Imbalance(ENTSOEBalancingLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, MarketBalanceArea):

        params = {
            'documentType':'A84',
            'processtype':'A16',
            'controlArea_Domain': MarketBalanceArea
            }
        response = self.client._base_request(params=params, start=self.start, end=self.end)
        print(response.text)        
        return response.text