import requests
import json
import pandas as pd
from datetime import datetime
#update pandas version
#print(pd.__version__)
#https://csgobackpack.net/api/

inv_id = 76561198162512099

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

    
def open_data():


    data = json.load(open('TEMP.json'))
    df = pd.DataFrame(data["items_list"])

    return df

def open_inv(inv_id):

    url = 'http://csgobackpack.net/api/GetInventoryValue/?id=' +str(inv_id)

    response = requests.get(url)
    print(response.status_code)    

    with open('TEMP.json','w') as f:
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        f.write(text)



#run_api()
open_inv(inv_id)
