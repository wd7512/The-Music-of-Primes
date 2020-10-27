import random
f = open('List.txt','r')
data = f.readlines()
f.close()
while True:
    var=input(random.choice(data))
