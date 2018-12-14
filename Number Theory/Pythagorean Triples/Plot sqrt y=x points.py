import matplotlib.pyplot as plt
import ast
y=open('Bounds=5000Power=0.5y=x.txt','r')
y1=y.readline()
y.close()
y1=ast.literal_eval(y1)
plt.plot(y1)
plt.show()
