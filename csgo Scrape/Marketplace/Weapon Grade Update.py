from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time

def collection(filename):
    f = open(filename,'r')
    data = f.readlines()
    f.close()
    inpdata = []
    for a in data[1:]:
        inpdata.append(a.split(','))

    guns = [a[0] for a in inpdata]
    gunsinput = []
    for a in guns:
        gun = []
        #print(a)
        b = a.split('|')
        #print(b)
        gun.append(b[0][:-1])
        c = b[1].split('(')
        #print(c)
        gun.append(c[0][1:-1])
        gun.append(c[1][:-1])
        gunsinput.append(gun)

    return [gunsinput,inpdata]
        


def lookup(gun,skin,wear):

    


    
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
    #driver.get('https://steamcommunity.com/market/listings/730/'+gun+'%20%7C%20'+skin+'%20%28'+wear+'%29')
    content = False
    while content == False:
        try:
            driver.get('https://steamcommunity.com/market/listings/730/'+gun+'%20%7C%20'+skin+'%20%28'+wear+'%29')
            content = driver.find_element_by_id("largeiteminfo_item_type")
        except NoSuchElementException:
            driver.quit()
            time.sleep(6)
    #print(content.text)

    grade = str(content.text)

    '''
    soup = BeautifulSoup(content)
    for a in soup.findAll('a',href=True):
        datall = str(a)
        print(datall)

        if '<div class="descriptor">Exterior: ' in datall:
            data = datall[datall.index('<div class="descriptor">Exterior: '):]
            data = data[:data.index('</div>')]
            #print(data)
            grade = data[34:]
    '''
    

    time.sleep(2)
    driver.quit()
    time.sleep(1)

    lisgrad = grade.split(' ')
    #print(lisgrad)
    output = ''
    output = output.join(lisgrad[:-1])


    return output

file = 'community_2.csv'
grades = []
guns,inpdata = collection(file)
for item in guns:
    grade = lookup(item[0],item[1],item[2])
    #print('this is')
    #print(grade)
    
    grades.append(grade)

label = ['Gun','Skin','Wear','Grade','Volume','Normal Price','Sale Price']
f = open('full_'+file,'w')
f.write('Gun,Skin,Wear,Grade,Volume,Normal Price,Sale Price\n')
for i in range(len(guns)):
    f.write(guns[i][0]+','+guns[i][1]+','+guns[i][2]+','+grades[i]+','+inpdata[i][-3]+','+inpdata[i][-2]+','+inpdata[i][-1])
    
f.close()

        
