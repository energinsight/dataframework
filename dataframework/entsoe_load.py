from.loaderAPI import DataLoader
# from entsoe import EntsoePandasClient
import os
import pandas as pd
import requests
import xml.etree.ElementTree as ET


class ENTSOELoad(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)
        api_key = os.getenv('ENTSOE_API_KEY')
        if not api_key:
            raise ValueError("Missing environment variable: ENTSOE_API_KEY")
        self.api_key = api_key
        self.url = "https://web-api.tp.entsoe.eu/api"
                
    def load_data(self):
        pass

class Total_DA_load(ENTSOELoad):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, area):
        url = self.url
        params = {
            'securityToken': self.api_key,
            'documentType': 'A65',
            'processType': 'A01',
            'outBiddingZone_Domain': area,
            'periodStart': self.start.strftime('%Y%m%d%H%M'),
            'periodEnd': self.end.strftime('%Y%m%d%H%M')
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            
            root = ET.fromstring(response.text)
            data = []
            for time_series in root.findall('.//{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}TimeSeries'):
                for period in time_series.findall('.//{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}Period'):
                    start = period.find('{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}timeInterval/{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}start').text
                    end = period.find('{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}timeInterval/{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}end').text
                    for point in period.findall('{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}Point'):
                        position = point.find('{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}position').text
                        quantity = point.find('{urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0}quantity').text
                        data.append({
                            'start': start,
                            'end': end,
                            'position': position,
                            'quantity': quantity
                        })
            df = pd.DataFrame(data)
            return df



        else:
            response.raise_for_status()