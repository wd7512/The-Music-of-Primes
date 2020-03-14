from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time

# float value equation
# (avg of inputs) * (range of output) + (output min) = output float
# so to get a certain output
# (avg of inputs) = ((output float) - (output min)) / (range of output)



def get_data(case):
    #case = 'Chroma-3-Case'
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

        nam = url[url.rfind('/')+1:]


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
        wears[0] = float(wearmin)
        wears[1] = float(wearmax)

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

        data.append([nam,rarity,wears,possible_wear,rec_price,listings,median,volume])

    return data

def tree_save(data,case):
    f = open(case + '_guns.csv','w')

    has_write = False
    while has_write == False:
        try:
            f.write('Name,Rarity,Price,Price x 10,Max Avg. Float input\n')
            has_write = True
        except PermissionError:
            nxt = input('File is currently open, please close and press enter:')
        

        
    for d in data:
        war = d[3]
        name = d[0]
        rarity = d[1][0]
        prices = d[4]
        wear_range = d[2]
        wear_min = wear_range[0]
        wear_diff = wear_range[1] - wear_range[0]
  
        for i in range(len(war)):
            w = war[i]
            
            count = 0
            fall = True
            while fall == True and type(prices[i+count]) != float:
                count = count+1

                if i+count+1 > len(prices):
                    fall = False
                
            if fall == True:    
                price = prices[i+count]
            else:
                price = 'n/a'

            flt_output = conv_wear(w)
            flt_input = (flt_output - wear_min) / wear_diff
            
            to_write = w + '_' + name + ',' + rarity + ',' + str(price) + ',' + str(price*10) + ',' + str(flt_input) + '\n'

            has_write = False
            while has_write == False:
                try:
                    f.write(to_write)
                    has_write = True
                except PermissionError:
                    nxt = input('File is currently open, please close and press enter:')
    f.close()
            
def conv_wear(strname):
    wear_ranges = [0.07,0.15,0.38,0.45,1.00]
    wear_names = ['Factory New','Minimal Wear','Field-Tested','Well-Worn','Battle-Scarred']

    i = wear_names.index(strname)
    return wear_ranges[i]
    
f = open('New_Collections.txt','r')
cases = f.readlines()
f.close()

cases_only = [c[c.rfind('/')+1:-1] for c in cases]
for case in cases_only:
    print(case)
    data = get_data(case)
    tree_save(data,case)
