import matplotlib.pyplot as plt
import math
f=open('PlistV2.txt','r')
maxx=len(f.readlines())
num=int(input('How many primes do we want to plot up to?\nthe max is '+str(maxx)+' type 0 for max\n:'))
f.close()
a=0
if num==0:
    num=maxx-1
def f(num):
    a=0
    f=open('PlistV2.txt','r')
    data=[]
    num=num+1
    while a!=num:# recieves data in str form
        data.append(f.readline())
        a=a+1
    f.close()
    plots=[]
    for i in range(len(data)):
        plots.append(i)
    for i in range(len(data)):# converts the list items into integers
        plots[i] = int(data[i])-int(data[i-1])
    counta=[]
    del plots[0]
    for i in plots:
        if i>(len(counta)-1):
            a=0
            b=i-len(counta)+1
            while a!=b:
                a=a+1
                counta.append(0)
        counta[i]=counta[i]+1
    tot=sum(counta)
    for i in range(len(counta)):
        counta[i]=counta[i]/tot
    product=0
    for i in range(len(counta)):
        product=product+i*counta[i]
    if sum(counta)==0:
        return(0)
    return(product/(sum(counta)))
y=[]
for i in range(num):
    y.append(f(i))
    print(str(i/num))
plt.plot(y)
plt.ylabel('prime numbers differance')
plt.show()
