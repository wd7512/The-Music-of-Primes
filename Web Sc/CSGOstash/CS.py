from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time


products = [] 
normal_prices = [] 
sale_prices = []
volume = []

f = open('Names.txt','r')
url = str(f.readline())
#print(url)
f.close()

driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
content = False
while content == False:
    try:
        driver.get(url)
        content = driver.find_element_by_class_name("well result-box nomargin")
    except NoSuchElementException:
        print('gsuifghsd')
        driver.quit()
        time.sleep(6)

print(str(content))
        
