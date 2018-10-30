import numpy as np
import matplotlib.pyplot as plt
import math
num=2*int(input('How many lines?'))
angle=math.pi/4
print(angle)
x=[]
y=[]
for i in range(num):
    if i%2==0:
        x.append(0)
        y.append((num-i)/2)
    else:
        x.append((i+1)/2)
        y.append(0)
x1=[]
y1=[]
for i in range(num):
    x1.append(x[i]*math.cos(angle)-y[i]*math.sin(angle))
    y1.append(x[i]*math.sin(angle)+y[i]*math.cos(angle))
for i in range(0, len(x), 1):
    plt.plot(x1[i:i+2], y1[i:i+2], 'r')
plt.axis('equal')
plt.show()
