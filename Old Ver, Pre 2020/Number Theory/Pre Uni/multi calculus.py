import math
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):

    if x!=0 and y!=0 and x*x!=y*y:
        
        return (x*x/y)
    else:
        return 0
    '''
    if x*y<1:
        return math.sqrt(1-x*y)
    else:
        return 0
    '''

lim=1
x=[]
for i in range((lim*2)*100+1):
    x.append(i/100-lim)
data=[]
for y in x:
    line=[]
    for x1 in x:
        line.append(f(x1,y))
    data.append(line)

plt.imshow(data)
plt.colorbar()

plt.show()
