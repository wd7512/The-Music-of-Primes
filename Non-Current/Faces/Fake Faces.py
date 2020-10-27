import random
import urllib.request

def download(url,filename):
    urllib.request.urlretrieve(url,filename)
url='https://thispersondoesnotexist.com/image'
download(url,'abc.jpeg')
