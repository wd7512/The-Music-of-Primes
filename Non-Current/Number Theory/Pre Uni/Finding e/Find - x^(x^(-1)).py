import matplotlib.pyplot as plt
import numpy as np
import math
acc=float(input('Using the theory that the maximun of the function:\nf(x)=x^(x^(-1)) is e\nwhat degree of accuray?'))
x=np.arange(2+acc,3,acc)
def f(x):
    return(x**(1/x))
y=[]
for i in range(len(x)):
    y.append(f(x[i]))
print(str(x[y.index(max(y))])+' is '+str(math.exp(1)-x[y.index(max(y))])+' off \n'+str(math.exp(1)))
plt.plot(x,f(x))
plt.show()
