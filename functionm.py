import matplotlib.pyplot as plt
import math

def f(x,y):
    if x==0 or y==0:
        return 0
    return ((x**-1)+(y**-1))**-1
length=1000
p=[]
for i in range(length):
    q=[]
    for j in range(length):
        q.append(f(i,j))
    p.append(q)
plt.imshow(p)
plt.show()
