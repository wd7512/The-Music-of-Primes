import ast
import matplotlib.pyplot as plt
import numpy as np
x1=[]
y1=[]
x2=[]
y2=[]
with open('TimeData.txt', 'r') as f:
    for line in f:
        line=ast.literal_eval(line)
        if line[1]=='XIAOMI' and len(line)==5:
            x1.append(line[2]/line[3])#calculations a second
            y1.append(line[4])#battery
x1=sorted(x1)
y1=sorted(y1)
plt.scatter(x1, y1, label='XIAOMI')
q=input('Lines of best fit?y/n\n:')
if q=='y':
    plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)))
plt.xlabel('Calculations/Second')
plt.ylabel('Battery %')
plt.legend()
plt.show()
