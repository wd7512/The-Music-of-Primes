import math
import matplotlib.pyplot as plt
import numpy as np
def ftest(n):
    if (2**(n-1))%n==1:
        return True
    return False
def btest(n):
    for i in range(int(math.sqrt(n)//1)):
        if n%(i+2)==0:
            return False
    return True
num=int(input('How many numbers do you want to go up to?'))
pseudo=[]
for i in range(num):
    if ftest(i+1)==True:
        print(i+1)
        if btest(i+1)!=True:
            print(str(i+1)+'Error')
            pseudo.append(i+1)
print(pseudo)
x=np.arange(0,num,1)
y=[0]
for i in range(len(x)-1):
    if i+1 in pseudo:
        y.append(y[i]+1)
    else:
        y.append(y[i])
plt.plot(x,y)
plt.show()
