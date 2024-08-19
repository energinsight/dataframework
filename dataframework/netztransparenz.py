import sys
import os
import requests
import pandas as pd
import json
from.loaderAPI import DataLoader

class netztransparenzDataLoader(DataLoader):
    def __init__(self, start, end):
        super().__init__(start, end)

    def load_data(self, url):
        pass

class reBAP(netztransparenzDataLoader):
        
        def load_data(self):
            
            # add your Client-ID and Client-secret from the API Client configuration GUI to
            # your environment variable first
            IPNT_CLIENT_ID = os.environ.get('IPNT_CLIENT_ID')
            IPNT_CLIENT_SECRET = os.environ.get('netztransparenz_Client_Secret')

            ACCESS_TOKEN_URL = "https://identity.netztransparenz.de/users/connect/token"


            # Ask for the token providing above authorization data
            response = requests.post(ACCESS_TOKEN_URL,
                            data = {
                                    'grant_type': 'client_credentials',
                                    'client_id': IPNT_CLIENT_ID,
                                    'client_secret': IPNT_CLIENT_SECRET
                    })

            # Parse the token from the response if the response was OK
            if response.ok:
                TOKEN = response.json()['access_token']
            else:
                print(f'Error retrieving token\n{response.status_code}:{response.reason}',
                    file = sys.stderr)
                exit(-1)

            # Provide URL to request health info on API
            myURL = "https://ds.netztransparenz.de/api/v1/health"

            Spot = "https://ds.netztransparenz.de/api/v1/data/Spotmarktpreise/2023-12-31T23%3A00%3A00/2024-01-31T23%3A00%3A00"
            reBAP = "https://ds.netztransparenz.de/api/v1/data/NrvSaldo/reBAP/Qualitaetsgesichert/2023-10-10T13%3A00%3A00/2023-11-10T13%3A00%3A00"


            response = requests.get(reBAP, headers = {'Authorization': 'Bearer {}'.format(TOKEN)})

            aa = response.text
            print(aa)
            #print(response.text, file = sys.stdout)
            return aa
        