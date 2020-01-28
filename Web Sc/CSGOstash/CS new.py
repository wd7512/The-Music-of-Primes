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
urls = f.readlines()

#print(url)
f.close()



'''
content = False
while content == False:
    try:
        driver.get(url)
        content = driver.find_element_by_class_name("col-lg-4 col-md-6 col-widen text-center")
    except NoSuchElementException:
        content = driver.page_source
        print('gsuifghsd')
        driver.quit()
        #time.sleep(6)

print(str(content))
'''

for url in urls:
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
    url = url[:-1]
    print(url)
    driver.get(url)
    content = driver.page_source
    driver.quit()

    links = []

    data = str(content)

    while "col-lg-4 col-md-6 col-widen text-center" in data:
        data = data[data.find("col-lg-4 col-md-6 col-widen text-center"):]
        for i in range(4):
            data = data[data.find('href')+1:]

        links.append(data[5:data.find('>')-1])
    f = open(url[31:]+'.txt','w')
    for link in links:
        f.write(link+'\n')
    f.close()
    #time.sleep(15)

