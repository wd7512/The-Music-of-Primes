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
y1=[0]
for i in range(n):#numbers of ones less than n
    if y[i]==5:
        y1.append(y1[i]+1)
    else:
        y1.append(y1[i])
y2=[0]
for i in range(n):#numbers of twos less than n
    if y[i]==6:
        y2.append(y2[i]+1)
    else:
        y2.append(y2[i])
y3=[0]
for i in range(n):#numbers of threes less than n
    if y[i]==7:
        y3.append(y3[i]+1)
    else:
        y3.append(y3[i])
y4=[0]
for i in range(n):#numbers of fours less than n
    if y[i]==8:
        y4.append(y4[i]+1)
    else:
        y4.append(y4[i])
plt.plot(x, y1, label='5 Factors')
plt.plot(x, y2, label='6 Factors')
plt.plot(x, y3, label='7 Factors')
plt.plot(x, y4, label='8 Factors')
plt.legend()
plt.show()
