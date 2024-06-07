import requests
from.loaderAPI import DataLoader

class JaoDataLoader(DataLoader):
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def load_data(self, url):
        pass

class JaoID2FinalNTC(JaoDataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)
    
    def load_data(self, params):
        params = {'fromUtc': self.start, 'toUtc': self.end}
        url = 'https://publicationtool.jao.eu/coreID/api/data/ID2_intradayNtc'
        data = requests.get(url, params=params)
        return data