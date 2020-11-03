import requests

#https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=9999999999
#gets all csgo items

url = 'https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=9999999999'

response = requests.get(url)
print(response.status_code)
