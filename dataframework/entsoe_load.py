from.loaderAPI import DataLoader
# from entsoe import EntsoePandasClient
import os
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from .utils import parse_xml_to_dataframe


class ENTSOELoad(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)
        api_key = os.getenv('ENTSOE_API_KEY')
        if not api_key:
            raise ValueError("Missing environment variable: ENTSOE_API_KEY")
        self.api_key = api_key
        self.url = "https://web-api.tp.entsoe.eu/api"
        self.documentType = {'total load': 'A65',
                             'Load forecast margin': 'A70'}
                
    def load_data(self):
        pass

class Total_DA_load(ENTSOELoad):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, area, documentType):
        url = self.url
        params = {
            'securityToken': self.api_key,
            'documentType': self.documentType[documentType],
            'processType': 'A01',
            'outBiddingZone_Domain': area,
            'periodStart': self.start.strftime('%Y%m%d%H%M'),
            'periodEnd': self.end.strftime('%Y%m%d%H%M')
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            
            namespaces = {'': 'urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0'}
            df = parse_xml_to_dataframe(response.content, namespaces)
            return df



        else:
            response.raise_for_status()