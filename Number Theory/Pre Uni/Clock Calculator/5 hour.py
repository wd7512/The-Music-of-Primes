import matplotlib.pyplot as plt
import numpy as np
num=int(input('How many number up to'))
clock=int(input('How many clocks up to'))
def y(x,d):
    return ((x**3-x)%d)
x=np.arange(0,num,1)
for i in range(clock):
    if i%2!=0 and i%3!=0:
        print(i)
        plt.plot(x,y(x,i), label=str(i))
plt.legend()
plt.show()
