import math
import matplotlib.pyplot as plt
import numpy as np
global expon
import cmath
import os.path
acc=float(input('What accuracy (<0.1)'))#degree of accuracy
if os.path.isfile('e-'+str(acc)+'.txt')==False:#create text file if there is one
    f=open('e-'+str(acc)+'.txt', 'w+')
    f.write('3')# first number of text file
    f.close()
with open('e-'+str(acc)+'.txt','r') as f:
    expon=float(f.readlines()[-1])# get last item of text file
def e(x):# function of estimated e
    return((expon**x).real)
def der(x):# function of derivitive of e
    return((e(x+acc/2)-e(x-acc/2))/acc)
def diff(x):# function to find common differance between function and derivitive
    return(der(x)/e(x))# also known as ln(expon)
x=np.arange(-10,5,acc) #creating array for x values
a=0
while a==0:
    print('The current estimate for e is: '+str(expon)+'\nthis is '+str(round(100*expon/math.exp(1)))+'% inaccurate')
    if diff(1)>1:
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
