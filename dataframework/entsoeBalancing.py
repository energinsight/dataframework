from.loaderAPI import DataLoader
# from entsoe import EntsoePandasClient
import requests
import os
import pandas as pd


class ENTSOEBalancingLoader(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)
        api_key = os.getenv('ENTSOE_API_KEY')
        if not api_key:
            raise ValueError("Missing environment variable: ENTSOE_API_KEY")
        self.api_key = api_key
        self.url = "https://web-api.tp.entsoe.eu/api"

    def load_data(self, params):
        # Load data from ENTSOE
        pass
        #return data


class Energy(ENTSOEBalancingLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, MarketBalanceArea, processtype, documentType):

        params = {
            'securityToken': self.api_key,
            'documentType': self.DocumentType[documentType],
            'processtype':self.ProcessType[processtype],
            'area_Domain': self.Areas[MarketBalanceArea],
            'periodStart': self.start.strftime('%Y%m%d%H%M'),
            'periodEnd': self.end.strftime('%Y%m%d%H%M')
            }
        response = requests.get(self.url, params=params)
        print(response.text)        
        return response.text