import matplotlib.pyplot as plt
import ast
import numpy as np

f=open('10000flips cut modify.txt','r')
data=f.readlines()
f.close()
x=[]
y=[]
for points in data:
    point=ast.literal_eval(points)
    x.append(point[0])
    y.append(point[1])
plt.plot(x,y,'o')
plt.axis('equal')
plt.xlabel('Original')
plt.ylabel('Shifted')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.show()
