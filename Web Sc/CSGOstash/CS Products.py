from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time


products = [] 
normal_prices = [] 
sale_prices = []
volume = []

case = 'Chroma-3-Case'
f = open(case + '.txt','r')
urls = f.readlines()

#print(url)
f.close()

wear_ranges = [0,0.07,0.15,0.38,0.45,1.00]
wear_names = ['Factory New','Minimal Wear','Field-Tested','Well-Worn','Battle-Scarred']

data = []

for url in urls:
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
    url = url[:-1]
    print(url)
    driver.get(url)
    content = driver.page_source
    driver.quit()

    name = url[url.rfind('/')+1:]


    wears = ['wearmin','wearmax']
    rec_price = ['STFN','STMW','STFT','STWW','STBS','FN','MW','FT','WW','BS']
    listings = ['STFN','STMW','STFT','STWW','STBS','FN','MW','FT','WW','BS']
    median = ['STFN','STMW','STFT','STWW','STBS','FN','MW','FT','WW','BS']
    volume = ['STFN','STMW','STFT','STWW','STBS','FN','MW','FT','WW','BS']
    rarity = ['']

    #Rarity
    ind = content.find('<p class="nomargin">') + 20
    rar1 = content[ind:]
    rar2 = rar1[:rar1.find(' ')]
    #print(rar2)
    rarity[0] = rar2
    
    #Wear
    wearnum = content.find('<div class="marker-value cursor-default"')
    wearmin = content[wearnum+146:wearnum+150]
    wearnum = content.find('data-wearmax=')
    wearmax = content[wearnum+14:wearnum+18]
    wears[0] = wearmin
    wears[1] = wearmax

    possible_wear = []
    index_wear = []
    for i in range(5):
        num_min = wear_ranges[i]
        num_max = wear_ranges[i+1]
        name = wear_names[i]
        if float(wearmin) <=num_max and float(wearmax) >= num_min:
            possible_wear.append(name)
            index_wear.append(i)
    

    var = len(index_wear)

    #Recent Price

    for i in range(var):
        w = possible_wear[i]
        a = content.find('StatTrak</span> '+w+'</td>')
        ref = content[a:]
        b = ref.find('rel="nofollow"')
        ref = ref[b+16:]
        ref = ref[:ref.find('<')]

        try:
            rec_price[index_wear[i]] = float(ref)
        except ValueError:
            pass

    for i in range(var):
        w = possible_wear[i]
        a = content.find('">'+w+'</td>')
        ref = content[a:]
        b = ref.find('rel="nofollow"')
        ref = ref[b+16:]
        ref = ref[:ref.find('<')]

        try:
            rec_price[index_wear[i]+5] = float(ref)
        except ValueError:
            pass

    #No. Listings

    #Median sale vale in last 24 hours

    #Volume sold in last 24 hours

    data.append([name,rarity,wears,possible_wear,rec_price,listings,median,volume])

def tree_save(data,case):
    f = open(case + '_guns.csv','w')
    f.write('Name,Rarity,Price,Price x 10')
    for d in data:
        war = d[3]
        name = d[0]
        rarity = d[1]
        prices = d[4]
  
        for i in range(len(war)):
            w = war[i]
            
            count = 0
            while type(prices[i+count]) != float:
                count = count+1
            price = prices[i+count]
            
            to_write = war + '_' + name + ',' + rarity + ',' + str(price) + ',' + str(price*10)
            f.write(to_write)
    f.close()
            
    
tree_save(data,case)
