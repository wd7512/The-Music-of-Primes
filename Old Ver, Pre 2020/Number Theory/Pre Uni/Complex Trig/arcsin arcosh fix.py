import math
import matplotlib.pyplot as plt
import numpy as np
# iarcsin(x)=arccosh(x)
def arccosh(lis):
    res=[]
    for x in lis:
        x=x.real
        print(x)
        if x<=0:
            res.append(0)
        else:
            res.append(math.log((x+math.sqrt(x*x-1))))
    return res
real=np.arange(0,.5*math.pi+.1,.1)
plt.plot(real,arccosh(real))
plt.xlabel('real')
plt.ylabel('imaginary')
plt.show()
