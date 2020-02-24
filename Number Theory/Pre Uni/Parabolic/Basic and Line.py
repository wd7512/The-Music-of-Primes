import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
num=2*int(input('How many lines?'))#2=2/3 3=2/2 4=6/5 5=6/4 10=30/11 9=2.5 99=25 
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
mid=(num/4)/(1+(num/4)/(num/4+1))#local minimun
print(mid)
plt.plot(mid,mid, 'ro')
plt.plot(np.arange(0,num/2,1), np.arange(0,num/2,1))
plt.axis('equal')
plt.show()
