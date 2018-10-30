import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
num=2*int(input('How many lines?'))
x=[]
y=[]
for i in range(num):
    if i%2==0:
        x.append(0)
        y.append((num-i)/2)
    else:
        x.append((i+1)/2)
        y.append(0)
for i in range(0, len(x), 2):
    plt.plot(x[i:i+2], y[i:i+2], 'r')
plt.axis('equal')
plt.show()
