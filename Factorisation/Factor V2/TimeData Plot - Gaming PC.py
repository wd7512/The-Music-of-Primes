import ast
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
with open('TimeData.txt', 'r') as f:
    for line in f:
        line=ast.literal_eval(line)
        x.append(line[2])
        y.append(line[3])
plt.scatter(sorted(x), sorted(y))
q=input('Line of best fit?y/n\n:')
if q=='y':
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'r')
plt.show()
