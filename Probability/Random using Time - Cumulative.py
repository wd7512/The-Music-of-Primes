import random
import matplotlib.pyplot as plt
import numpy as np
import time

limnum=2000
runs=100000
period=10**(-10)

def random1(list1,period):
    t = time.time()
    i=0
    while time.time()-t<period:
        if i==list1[-1]:
            i=0
        else:
            i=i+1
    return list1[i]

a=[]

for i in range(limnum):
    a.append(i)

x1=np.arange(0,limnum,1)
x2=x1

z1=[]
z2=[]

for i in range(runs):
    z1.append(random1(a,period))
    z2.append(random.randint(0,limnum-1))

y1=[]
y2=[]

for i in range(limnum):
    y1.append(z1.count(i))
    y2.append(z2.count(i))
    

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.ylabel('Time Random')
#plt.axis('Equal')
#plt.ylim(bottom=runs/(2*limnum))
#plt.ylim(top=3*runs/(2*limnum))


plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.ylabel('Import Random')
#plt.axis('Equal')
plt.ylim(bottom=runs/(2*limnum))
plt.ylim(top=3*runs/(2*limnum))

plt.show()

