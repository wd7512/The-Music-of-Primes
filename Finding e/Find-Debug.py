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
    print('e')
    print(str(expon)+'**'+str(x)+'='+str(expon**x))
    return((expon**x).real)
def der(x):
    print('der')
    print(str(e(x+acc/2))+'-'+str(e(x-acc/2))+'/'+str(acc)+'='+str((e(x+acc/2)-e(x-acc/2))/acc))
    return((e(x+acc/2)-e(x-acc/2))/acc)
def diff(x):
    print('diff')
    print(str(der(x))+'/'+str(e(x))+'='+str(der(x)/e(x)))
    return(der(x)/e(x))
runs=int(input('How many runs?'))
x=np.arange(-10,5,acc)
for i in range(runs):
    print('The current estimate for e is: '+str(expon)+'\nthis is '+str(round(100*expon/math.exp(1)))+'% inaccurate')
    if diff(3)>1:
        expon=expon-acc
    else:
        expon=expon+acc
    print('Testing '+str(expon))
    with open('e-'+str(acc)+'.txt', 'a') as f:
        f.write('\n'+str(expon))
plt.plot(x,e(x), label=('function'))
plt.plot(x,der(x), label=('differential'))
plt.plot(x,diff(x), label=('differance'))
plt.legend()
plt.show()
