import requests
import json
import pandas as pd



key = str(input('API Key: '))

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def jsave(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    with open('TEMP.json','w') as f:
        f.write(str(text))

class tftplayer:
    def __init__(self,api_key,username):
        self.key = api_key
        self.summonerName = username

        url = 'https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-name/'+self.summonerName+'/?api_key=' + self.key
        response = requests.get(url)
        self.details = response.json()


    def get_match_history(self,n):
        url = 'https://europe.api.riotgames.com/tft/match/v1/matches/by-puuid/'+self.details['puuid']+'/ids?count='+str(n)+'&api_key='+ self.key
        response = requests.get(url)
        self.history = response.json()

    def get_match(self,matchId):
        url = 'https://europe.api.riotgames.com/tft/match/v1/matches/'+matchId+'?api_key=' + self.key
        response = requests.get(url)
        self.match = response.json()

        data = self.match['info']['participants']
        for element in data:
            
            element.pop('companion')
            element.pop('traits')
            element.pop('units')
        jprint(data)
        

        self.df = pd.DataFrame(data)

        
        

    
        
a = tftplayer(key,'wd7512')
a.get_match_history(10)
a.get_match(a.history[0])

