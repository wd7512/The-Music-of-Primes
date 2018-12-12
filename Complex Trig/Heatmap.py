import math
import matplotlib.pyplot as plt
import numpy as np

def f(y,x):
    z=(x-y*1j)**6
    return float(z.imag)

def high(a):
    list1=[]
    for i in a:
        list1.append(max(i))
    return max(list1)

def low(a):
    list1=[]
    for i in a:
        list1.append(min(i))
    return min(list1)

num=10
interval=.1
prod=num/interval
a=[]

for i in range(int((prod)+1)):
    a.append([f(i*interval,0)])
    for j in range(int(prod)):
        a[i].append(f(i*interval,(j+1)*interval))
    print(str(100*i/(prod))+'%')
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.xlabel('zoom=x'+str(interval)+'  0-'+str(num))
plt.ylabel('zoom=x'+str(interval)+'  0-'+str(num))
plt.gca().invert_yaxis()

bar=[low(a),(low(a)+high(a))/2,high(a)]

plt.colorbar(ticks=bar)
plt.show()
