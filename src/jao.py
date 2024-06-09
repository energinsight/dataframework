import requests
from.loaderAPI import DataLoader

class JaoDataLoader(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, url):
        pass

class JaoID2FinalNTC(JaoDataLoader):
    
    def load_data(self):
        params = {'fromUtc': self.start, 'toUtc': self.end}
        url = 'https://publicationtool.jao.eu/coreID/api/data/ID2_intradayNtc'
        data = requests.get(url, params=params)
        return data