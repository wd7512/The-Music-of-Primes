from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


products = [] 
normal_prices = [] 
sale_prices = []
volume = []


search = 'community_1'
pagenum_total = 11

def scrap(search,pagenum):

    
    products = [] 
    normal_prices = [] 
    sale_prices = []
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
    #driver.get('https://steamcommunity.com/market/search?appid=730&q='+search+'#p'+str(pagenum)+'_price_asc')
    #general search
    #driver.get('https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=tag_weapon_'+weapon+'&appid=730#p'+str(pagenum)+'_price_asc')
    #specific gun
    driver.get('https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_'+search+'&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&appid=730#p'+str(pagenum)+'_price_asc')
    #collection
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('a',href=True):
        #print(a)
        datall = str(a)
        
        
        if '<span class="market_listing_item_name"' in datall:
            data = datall[datall.index('<span class="market_listing_item_name"'):]
            data = data[:data.index('</span>')]
            #print(data)
            point = data.index('>')
            products.append(data[point+1:])

        if '<span class="normal_price"' in datall:
            data = datall[datall.index('<span class="normal_price"'):]
            data = data[:data.index('</span>')]
            #print(data)
            point = data.index('>')
            normal_prices.append(data[point+1:])

        if '<span class="sale_price"' in datall:
            data = datall[datall.index('<span class="sale_price"'):]
            data = data[:data.index('</span>')]
            #print(data)
            point = data.index('>')
            sale_prices.append(data[point+1:])

        if '<span class="market_listing_num_listings_qty" data-qty="' in datall:
            data = datall[datall.index('<span class="market_listing_num_listings_qty" data-qty="')+56:]
            data = data[:data.index('">')]
            #print(data)
            volume.append(data)

    
    
    time.sleep(2)
    driver.quit()
    time.sleep(1)
    return [products,normal_prices,sale_prices]
    

for i in range(pagenum_total):
    runn = scrap(search,i+1)

    #print(runn)

    while runn[0] == []:
        time.sleep(15)
        runn = scrap(search,i+1)

    products = products + runn[0]
    normal_prices = normal_prices + runn[1]
    sale_prices = sale_prices + runn[2]
    



output = list(zip(products,volume,normal_prices,sale_prices))
for item in output:
    print(item)

f = open(search+'.csv','w')
f.write('Product,Volume,Normal Price,Sale Price\n')
for a in output:
    if a[0][-4:] == 'Case' or a[0][-3:] == 'Key':
        pass
    else:
        f.write(a[0]+','+a[1]+','+a[2]+','+a[3]+'\n')
    '''
    name = a[0]
    nam = name.split('|')
    if len(nam) == 2:
        f.write(nam[0][:-1]+','+nam[1][1:]+','+a[1]+','+a[2]+'\n')
    '''

f.close()

