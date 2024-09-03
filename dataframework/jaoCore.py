import requests
import pandas as pd
import json
from.loaderAPI import DataLoader

class Jao_core(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, url):
        pass

class Jaocore_maxnetposition(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/maxNetPos'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df

class Jaocore_maxbex(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/maxExchanges'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        
class Jaocore_bexrestriction(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/bexRestrictions'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df

class Jaocore_allocationconstraint(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/allocationConstraint'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class Jaocore_d2cf(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/d2CF'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class Jaocore_refprog(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/refprog'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df

        
class Jaocore_referencenetposition(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/referenceNetPosition'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class Jaocore_atconcoreexternalborders(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/atc'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df

class Jaocore_shadowauctionatc(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/shadowAuctionAtc'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df


class Jaocore_shadowprices(Jao_core):
        
        def load_data(self):
            params =  {
            "Filter": {},
            "Skip": 0,
            "Take": 1000,
            "FromUtc": self.start.isoformat(),
            "ToUtc": self.end.isoformat()
            }

            url = 'https://publicationtool.jao.eu/core/api/data/shadowPrices'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df



class Jaocore_congestionincome(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/congestionIncome'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df


class Jaocore_scheduledexchanges(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/scheduledExchanges'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df

class Jaocore_netposition(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/netPos'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class Jaocore_pricespread(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/priceSpread'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class Jaocore_alphafactor(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/alphaFactor'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df


class Jaocore_remedialactionpreventive(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/pra'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        


class Jaocore_remedialactioncurative(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/cra'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class Jaocore_ltn(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/ltn'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class Jaocore_lta(Jao_core):
        
        def load_data(self):
            params =  {
                "FromUtc": self.start.isoformat(),
                "ToUtc": self.end.isoformat()
                }

            url = 'https://publicationtool.jao.eu/core/api/data/lta'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df

class Jaocore_validationreduction(Jao_core):
        
        def load_data(self):
            params =  {
            "Filter": json.dumps({"Presolved": True}),
            "Skip": 0,
            "Take": 1000,
            "FromUtc": self.start.isoformat(),
            "ToUtc": self.end.isoformat()
            }

            url = 'https://publicationtool.jao.eu/core/api/data/validationReductions'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        

class Jaocore_prefinal(Jao_core):
        
        def load_data(self):
            params =  {
            "Filter": json.dumps({"Presolved": True}),
            "Skip": 0,
            "Take": 1000,
            "FromUtc": self.start.isoformat(),
            "ToUtc": self.end.isoformat()
            }

            url = 'https://publicationtool.jao.eu/core/api/data/preFinalComputation'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df
        


        
class Jaocore_initialcomputation(Jao_core):
        
        def load_data(self):
            params =  {
            "Filter": json.dumps({"Presolved": True}),
            "Skip": 0,
            "Take": 1000,
            "FromUtc": self.start.isoformat(),
            "ToUtc": self.end.isoformat()
            }

            url = 'https://publicationtool.jao.eu/core/api/data/initialComputation'
            data = requests.get(url, params=params)

            json_data = data.json()
            df = pd.DataFrame(json_data['data'])
            df.set_index('dateTimeUtc', inplace=True)
    
            return df




class Jaocore_finalcomputation(Jao_core):
        
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