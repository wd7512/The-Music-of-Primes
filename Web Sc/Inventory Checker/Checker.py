from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

f = open('Invent.txt','r')
urls = f.readlines()
f.close()
url = urls[0]

connection = False

while connection == False:
    try:
        driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
        connection = True
    except WebDriverException:
        pass
print(url)
driver.get(url)
located = False
items = []
content = driver.page_source
locator = 'div class="itemHolder"'
driver.quit()
