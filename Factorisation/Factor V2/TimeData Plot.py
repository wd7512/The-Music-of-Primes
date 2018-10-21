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
        if line[1]=='XIAOMI':
            x1.append(line[2])
            y1.append(line[3])
        if line[1]=='GAMINGPC':
            x2.append(line[2])
            y2.append(line[3])
plt.scatter(sorted(x1), sorted(y1), label='XIAOMI')
plt.scatter(sorted(x2), sorted(y2), label='GAMINGPC')
q=input('Lines of best fit?y/n\n:')
if q=='y':
    plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)), 'r')
    plt.plot(np.unique(x2), np.poly1d(np.polyfit(x2, y2, 1))(np.unique(x2)), 'r')
plt.legend()
plt.show()
