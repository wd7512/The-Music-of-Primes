import matplotlib.pyplot as plt
import ast
f=open('Clock Results - Overtime.txt','r')
data=f.readlines()
f.close()
x=[]
y=[]
for point in data:
    point=ast.literal_eval(point)
    x.append(point[0])
    y.append(point[1])
plt.plot(x,y)
plt.show()
