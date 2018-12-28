import matplotlib.pyplot as plt
import ast
f=open('Clock Results - Overtime.txt','r')
data=f.readlines()
f.close()
x=[]
y=[]
for point in data:
    point=ast.literal_eval(point)
    if point[0]%100000==0:
        
        x.append(point[0])
        y.append(point[1])
plt.plot(x,y)
plt.show()
