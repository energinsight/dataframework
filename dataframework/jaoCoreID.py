import requests
import pandas as pd
import json
from.loaderAPI import DataLoader

class Jao_coreID(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, url):
        pass




###################### IDCCB ############################
class IDCCB_refprog(Jao_coreID):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_refprog'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df

    
class IDCCB_maxnetposition(Jao_coreID):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_maxNetPos'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class IDCCB_maxbex(Jao_coreID):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_maxExchanges'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class IDCCB_initialcomputation(Jao_coreID):
        
        def load_data(self):
            params =  {
            "Filter": json.dumps({"Presolved": True}),
            "Skip": 0,
            "Take": 1000,
            "FromUtc": self.start.isoformat(),
            "ToUtc": self.end.isoformat()
            }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_initialComputation'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df



class IDCCB_validationreductions(Jao_coreID):
        def load_data(self):
            params =  {
                "Filter": {},
                "Skip": 0,
                "Take": 1000,
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_validationReductions'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df


class IDCCB_finalcomputation(Jao_coreID):
        
        def load_data(self):
            params =  {
            "Filter": json.dumps({"Presolved": True}),
            "Skip": 0,
            "Take": 1000,
            "FromUtc": self.start.isoformat(),
            "ToUtc": self.end.isoformat()
            }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_finalComputation'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df

      
class IDCCB_usedgridmodel(Jao_coreID):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_CGM'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df


class IDCCB_referencenetposition(Jao_coreID):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_referenceNetPosition'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        
class IDCCB_finalatcforsidc(Jao_coreID):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_intradayAtc'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class IDCCB_finalntcforsidc(Jao_coreID):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/coreID/api/data/IDCCB_intradayNtc'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        
        

'''
class ID2_intradayNtc(Jao_coreID):
    
    def load_data(self):
        params = {'fromUtc': self.start, 'toUtc': self.end}
        url = 'https://publicationtool.jao.eu/coreID/api/data/ID2_intradayNtc'
        data = requests.get(url, params=params)
        data1 = pd.DataFrame(data.json())
        aa = data1['data']

        # Convert each dictionary in aa into a DataFrame
        dfs = [pd.DataFrame([dict_], columns=dict_.keys()) for dict_ in aa]

        # Concatenate all DataFrames
        df = pd.concat(dfs, ignore_index=True)

        # Convert the 'dateTimeUtc' column to datetime
        df['dateTimeUtc'] = pd.to_datetime(df['dateTimeUtc'])

        # Set 'dateTimeUtc' as the index
        df.set_index('dateTimeUtc', inplace=True)

        return df
'''