import math
import matplotlib.pyplot as plt
import numpy as np
global expon
import cmath
import os.path
acc=2
if os.path.isfile('e-V2.txt')==False:
    f=open('e-V2.txt', 'w+')
    f.write('3')
    f.close()
with open('e-V2.txt','r') as f:
    expon=float(f.readlines()[-1])
def e(x, expon):
    return((expon**x).real)
def der(x, expon):
    return((e(x+acc/2, expon)-e(x-acc/2, expon))/acc)
def diff(x, expon):
    return(der(x, expon)/e(x, expon))
def prog(acc, expon):
    if acc<.000001:
        print('-10,'+str(-10+(.0000001/acc))+','+str(acc))
        x=np.arange(-10,(-10+(.0000001/acc),acc))
        for i in range((.000001/acc)*14):
            x=np.concatenate((x,np.arange(-10+((i+1)*(.000001/acc)),(-10+((i+2)*(.000001/acc)),acc))),axis=0)
    else:     
        x=np.arange(-10,5,acc)
    a=0
    while a==0:
        print('The current estimate for e is: '+str(expon)+'\nthis is '+str(round(100*expon/math.exp(1)))+'% inaccurate')
        if diff(3, expon)>1:
            expon=expon-acc
        else:
            expon=expon+acc
        print('Testing '+str(expon))
        with open('e-V2.txt', 'a') as f:
            f.write('\n'+str(expon))
        with open('e-V2.txt', 'r') as f:
            b=list(f.readlines())
            if len(b)>3:
                if (float(b[-1])/math.exp(1))<1 and (float(b[-2])/math.exp(1))>1:
                    a=a+1
                    acc=2*(10**(round(math.log10(.1*acc))))
                    print(acc)
                    if expon==math.exp(1):
                        print('Finished')
                        plt.plot(x,e(x), label=('function'))
                        plt.plot(x,der(x), label=('differential'))
                        plt.plot(x,diff(x), label=('differance'))
                        plt.legend()
                        plt.show()
                    else:
                        prog(acc, expon)
prog(acc, expon)
