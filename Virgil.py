import urllib.request

var = urllib.request.urlopen('https://bath.libcal.com/r/new/availability?lid=1642&zone=0&gid=3007&capacity=1')

data = str(var.read())

with open('TEMP.txt','w') as f:
    f.write(data)


