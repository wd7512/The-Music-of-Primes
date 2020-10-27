import numpy as np
import matplotlib.pyplot as plt
import math
num=2*int(input('How many lines?'))
angle=math.pi/4
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
def poly(a, root, mid):
    F=mid*math.sin(angle)+mid*math.cos(angle)
    return(F*(a**2)/(root)**2+F)#max y is max(x1)+max(x1)/num
x2=np.arange(min(x1),max(x1),.1)
plt.plot(x2,poly(x2,max(y1),(num/4)/(1+(num/4)/(num/4+1))))
#min(x1) is the "roots" and mid is the non rotated minimun
plt.axis('equal')
plt.show()
