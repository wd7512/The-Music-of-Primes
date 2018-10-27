import math
import matplotlib.pyplot as plt
import numpy as np
global expon
import cmath
import os.path
acc=float(input('What accuracy (<0.1)'))
if os.path.isfile('e-'+str(acc)+'.txt')==False:
    f=open('e-'+str(acc)+'.txt', 'w+')
    f.write('3')
    f.close()
with open('e-'+str(acc)+'.txt','r') as f:
    expon=float(f.readlines()[-1])
def e(x):
    return((expon**x).real)
def der(x):
    return((e(x+acc/2)-e(x-acc/2))/acc)
def diff(x):
    return(der(x)/e(x))
x=np.arange(-10,5,acc)
a=0
while a==0:
    print('The current estimate for e is: '+str(expon)+'\nthis is '+str(round(100*expon/math.exp(1)))+'% inaccurate')
    if diff(3)>1:
        expon=expon-acc
    else:
        expon=expon+acc
    print('Testing '+str(expon))
    with open('e-'+str(acc)+'.txt', 'a') as f:
        f.write('\n'+str(expon))
    with open('e-'+str(acc)+'.txt', 'r') as f:
        b=list(f.readlines())
        if len(b)>3:
            if float(b[-1])==float(b[-3]):
                a=a+1
plt.plot(x,e(x), label=('function'))
plt.plot(x,der(x), label=('differential'))
plt.plot(x,diff(x), label=('differance'))
plt.legend()
plt.show()
