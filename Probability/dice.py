import random
import matplotlib.pyplot as plt

rolls=100000
numofdice=6

def roll(numofdice):
    total=0
    for i in range(numofdice):
        total=total+random.randint(1,6)
        
    return total

maxi=numofdice*6

x=[]
y=[]
for i in range(maxi):
    x.append(i+1)
    y.append(0)
    
for i in range(rolls):
    num=roll(numofdice)
    y[num-1]=y[num-1]+1

plt.bar(x,y)
plt.show()
