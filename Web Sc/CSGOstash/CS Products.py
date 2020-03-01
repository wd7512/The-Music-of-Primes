from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time


products = [] 
normal_prices = [] 
sale_prices = []
volume = []

f = open('Chroma-3-Case.txt','r')
urls = f.readlines()

#print(url)
f.close()

wear_ranges = [0.07,0.15,0.38,0.45,1.00]

wears = []
for url in urls:
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
    url = url[:-1]
    print(url)
    driver.get(url)
    content = driver.page_source
    driver.quit()

    #Wear
    wearnum = content.find('<div class="marker-value cursor-default"')
    wearmin = content[wearnum+146:wearnum+150]
    wearnum = content.find('data-wearmax=')
    wearmax = content[wearnum+14:wearnum+18]
    wears.append([wearmin,wearmax])

    #Lowest Price

    #No. Listings

    #Median sale vale in last 24 hours

    #Volume sold in last 24 hours

    
