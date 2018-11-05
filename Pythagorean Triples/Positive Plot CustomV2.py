import numpy as np
import matplotlib.pyplot as plt
from decimal import *
length=int(input('Bounds?\n:'))
power=float(input('Power?\n:'))
acc=input('Accuracy?(<1)\n:')
exp=[1]
for i in range(length+1):#i=x
    if round(100*i/(length+1))!=round(100*(i-1)/(length+1)):
        print(str(round(100*i/(length+1)))+'% calculated')
    for j in range(length+1):#j=y
        #print(str(i**power)+'+'+str(j**power)+')^'+str(1/power)+'%1='+str(Decimal((i**power+j**power)**(1/power)).quantize(Decimal('0.0000001'))%1))
        if Decimal((i**power+j**power)**(1/power)).quantize(Decimal(acc))%1==0 and i!=0 and j!=0:
            plt.plot(i,j, 'ro')
            if i==j:#function e.g x[i]=y[i]
                if exp[-1]!=i:
                    exp.append(i)
null=[]
for _ in range(length+1):
    null.append(0)
f=open('Bounds='+str(length)+'Power='+str(power)+'y=x.txt','w')
f.write(str(exp))
f.close()
plt.plot(np.arange(0,length+1,1),null,'b')
plt.plot(null,np.arange(0,length+1,1),'b')
plt.grid(True)
plt.axis('Equal')
print(exp)
plt.show()
