import numpy as np
import matplotlib.pyplot as plt
length=int(input('Bounds?\n:'))
x=np.arange(-length,length+1,1)
y=np.arange(-length,length+1,1)
for i in range(length*2+1):
    print(str(round(100*i/(length*2+1)))+'% calculated')
    for j in range(length*2+1):
        if np.sqrt((x[i])**2+y[j]**2)%1==0 and x[i]!=0 and y[j]!=0:
            plt.plot(x[i],y[j], 'ro')
null=[]
for _ in range(length*2+1):
    null.append(0)
plt.plot(np.arange(-length,length+1,1),null,'b')
plt.plot(null,np.arange(-length,length+1,1),'b')
plt.grid(True)
plt.show()
