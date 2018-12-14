import math
import matplotlib.pyplot as plt
import numpy as np
global power
power=.01
plt.title('Re['+str(power)+'^(x+yi)]')
def f(y,x):
    global power
    return float((power**(x+y*1j)).real)

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

num=math.pi*2
interval=.01
prod=num/interval
a=[]

for i in range(int((prod)+1)):
    a.append([f(i*interval,0)])
    for j in range(int(prod)):
        a[i].append(f(i*interval,(j+1)*interval))
    print(str(100*i/(prod))+'%')
plt.imshow(a, cmap='terrain', interpolation='nearest')
plt.xlabel('zoom=x'+str(interval)+'  0-'+str(num))
plt.ylabel('zoom=x'+str(interval)+'  0-'+str(num))
plt.gca().invert_yaxis()

bar=[low(a),(low(a)+high(a))/2,high(a)]

plt.colorbar(ticks=bar)

#plt.savefig(str(power)+'.png')

plt.show()
