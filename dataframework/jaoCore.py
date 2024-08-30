import requests
import pandas as pd
import json
from.loaderAPI import DataLoader

class Jao_core(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, url):
        pass


class JaoDAfinalcomputation(Jao_core):
        
        def load_data(self):
            params =  {
            "Filter": json.dumps({"Presolved": True}),
            "Skip": 0,
            "Take": 1000,
            "FromUtc": self.start.isoformat(),
            "ToUtc": self.end.isoformat()
            }

            url = 'https://publicationtool.jao.eu/core/api/data/finalComputation'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df