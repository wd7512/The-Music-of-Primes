import matplotlib.pyplot as plt
import ast
y=open('Bounds=5000Power=0.5y=x.txt','r')
y1=y.readline()
y.close()
y1=ast.literal_eval(y1)
y2=[0]
for i in range(len(y1)-1):
    y2.append(y1[i+1]-y1[i])
plt.plot(y2)
plt.show()
