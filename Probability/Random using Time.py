import random
import matplotlib.pyplot as plt
import numpy as np
import time




def random1(list1):
    t = time.time()
    i=0
    while time.time()-t<(10**(-100)):
        if i==list1[-1]:
            i=0
        else:
            i=i+1
    return list1[i]

a=[0,1,2,3,4,5,6,7,8,9]

x1=np.arange(0,100,1)
x2=x1

y1=[]
y2=[]

for i in range(100):
    y1.append(random1(a))
    y2.append(random.randint(0,9))

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.ylabel('Time Random')


plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.ylabel('Import Random')

plt.show()

