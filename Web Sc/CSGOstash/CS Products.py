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

wears = []
for url in urls:
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
    url = url[:-1]
    print(url)
    driver.get(url)
    content = driver.page_source
    driver.quit()
    wearnum = content.find('<div class="marker-value cursor-default"')
    wearmin = content[wearnum+146:wearnum+150]
    wearnum = content.find('data-wearmax=')
    wearmax = content[wearnum+14:wearnum+18]
    wears.append([wearmin,wearmax])
