import math
import matplotlib.pyplot as plt
import numpy as np
#sinh(ix)=isin(x)
def sinh(x):
    return (math.e**(x)-math.e**(-x))/2
def sin(x):
    return math.sin(x)
real=np.arange(0,2*math.pi+.1,.1)
plt.plot(real,sinh(real*1j).imag)
plt.show()
