import matplotlib.pyplot as plt
import ast
#plots the % found in each 100,000 chunk
f=open('Clock Results - Overtime.txt','r')
data=f.readlines()
f.close()
x=[]
y=[]
z=[]
for point in data:
    point=ast.literal_eval(point)
    if point[0]%100000==0:
        #print(point)
        x.append(point[0])
        y.append(point[1])
for i in range(len(y)):
    if i==0:
        z.append(y[0])
    else:
        num=(i+1)*y[i]-i*y[i-1]
        z.append(num)

plt.plot(x,z, 'r')
plt.plot(x,y)
plt.show()
