import requests
import json
import pandas as pd
from datetime import datetime
#update pandas version
#print(pd.__version__)
#https://csgobackpack.net/api/



#https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=9999999999
#gets all csgo items

def run_api():
    
    url = 'https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=9999999999'
    url = 'http://csgobackpack.net/api/GetItemsList/v2/'

    response = requests.get(url)
    print(response.status_code)



    with open('TEMP.json','w') as f:
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        f.write(text)

    





run_api()
