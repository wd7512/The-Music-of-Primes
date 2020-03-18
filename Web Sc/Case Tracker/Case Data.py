from selenium import webdriver
import time
from datetime import datetime

# float value equation
# (avg of inputs) * (range of output) + (output min) = output float
# so to get a certain output
# (avg of inputs) = ((output float) - (output min)) / (range of output)



def get_data(urls):

    


    
    data = []

    for url in urls:
        driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
        print(url)
        driver.get(url)
        content = driver.page_source
        driver.quit()

        name = url[url.rfind('/')+1:]
        

        cut = cut_find_text('<span class="pull-right">',content,0)
        cut = cut_find_text('<span class="pull-right">',cut,0)
        Listings = cut_find_text('<span class="pull-right">',cut,0)
        Median = cut_find_text('<span class="pull-right">',Listings,0)
        Volume = cut_find_text('<span class="pull-right">',Median,0)

        Listings = int(Listings[:Listings.find('<')])
        Median = float(Median[:Median.find('<')].replace('£',''))
        Volume = int(Volume[:Volume.find('<')])

        data.append([name,Listings,Median,Volume])

    return data


def cut_find_text(text,data,reverse): #cuts string to end of first text
    a = data.find(text)

    if reverse == True or reverse == 1:
        return data[:a]
    else:
        return data[a+len(text):]

def get_time():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    dt = date_time.replace(' ',',')
    return dt
    

def update():

    urls = get_urls()
    data = get_data(urls)

    dt = get_time()
    

    f = open('Listings.csv','a')
    Listings = ','.join(str(d[1]) for d in data)
    to_write = dt + ',' + Listings + '\n'
    f.write(to_write)
    f.close()

    f = open('Medians.csv','a')
    Medians = ','.join(str(d[2]) for d in data)
    to_write = dt + ',' + Medians + '\n'
    f.write(to_write)
    f.close()

    f = open('Volumes.csv','a')
    Volumes = ','.join(str(d[3]) for d in data)
    to_write = dt + ',' + Volumes + '\n'
    f.write(to_write)
    f.close()
    
    

    

def get_urls():
    f = open('Case Links.txt','r')
    cases = f.readlines()
    f.close()
    urls = []
    for c in cases:
        urls.append(c.replace('\n',''))

    return urls
    
def clean_set_up():
    
    urls = get_urls()
    names = [url[url.rfind('/')+1:] for url in urls]

    files = ['Volumes.csv',
             'Listings.csv',
             'Medians.csv']

    str_names = ','.join(names)

    for file in files:
        f = open(file,'w')
        f.write('Date,Time,'+str_names+'\n')
        f.close()
        
    
urls = get_urls()
update()
while True:
    time.sleep(15)
    tim = get_time()
    print(tim)
    mini = tim[-5:-3]
    if int(mini) % 10 == 0:
        update()
