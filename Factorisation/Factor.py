import math
import matplotlib.pyplot as plt
n=int(input('How many numbers do you want to go up to?\nn:'))
x=[]
for i in range(n+1):
    x.append(i)
f=open('PlistV2.txt','r')
primelist=f.readlines()
f.close()
for i in range(len(primelist)):
    primelist[i]=int(primelist[i])
y=[]
for i in range(n+1):
    a=0
    b=0
    while primelist[b]<=math.floor((x[i]/2)):
        if x[i]%primelist[b]==0:
            a=a+1
        b=b+1
    if a==0:
        y.append(1)
    else:
        y.append(a)
plt.plot(x, y)
plt.show()
