from.loaderAPI import DataLoader
# from entsoe import EntsoePandasClient
import os
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from .utils import parse_xml_to_dataframe


class ENTSOEGeneration(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)
        api_key = os.getenv('ENTSOE_API_KEY')
        if not api_key:
            raise ValueError("Missing environment variable: ENTSOE_API_KEY")
        self.api_key = api_key
        self.url = "https://web-api.tp.entsoe.eu/api"
        self.documentType = {'Installed generation per type': 'A68',
                             'Reservoir filling information': 'A72',
                             'Actual generation per type': 'A75',
                             'Actual generation': 'A73',
                             'Generation forecast': 'A71',
                             'Wind and solar forecast': 'A69'}
        self.ProcessType = {'Day ahead': 'A01',
                            'Realised': 'A16',
                            'Week ahead': 'A31',
                            'Month ahead': 'A32',
                            'Year ahead': 'A33',}
                
    def load_data(self, area, documentType = 'Actual generation', ProcessType = 'Realised', PsrType = None):
        url = self.url
        params = {
            'securityToken': self.api_key,
            'documentType': self.documentType[documentType],
            'processType': self.ProcessType[ProcessType],
            'In_Domain': area,
            'PsrType': PsrType,
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