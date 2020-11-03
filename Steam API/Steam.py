import requests
import json
import pandas as pd
from datetime import datetime
#update pandas version
print(pd.__version__)



#https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=9999999999
#gets all csgo items

def run_api():
    
    url = 'https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=9999999999'

    response = requests.get(url)
    print(response.status_code)



    with open('TEMP.json','w') as f:
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        f.write(text)

    

def open_data():
    

    data = json.load(open('TEMP.json'))
    df = pd.DataFrame(data["results"])

    return df

def add_row(data):

    if len(data) != 100 or type(data) != list:
        print('Data Invalid')
    else:

        now = datetime.now()

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        data = [str(dt_string)] + data
        
        with open('Data.csv','a') as f:
            text = str(data)
            text = text.replace('[','')
            text = text.replace(']','')
            text = text.replace('"','')
            text = text.replace("'",'')

            f.write(text + '\n')



run_api()
a = open_data()
prices = a['sell_price']
add_row(list(prices))
