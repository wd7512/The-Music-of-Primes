import numpy as np
import matplotlib.pyplot as plt
length=int(input('Bounds?\n:'))
power=float(input('Power?\n:'))
x=np.arange(0,length+1,1)
y=np.arange(0,length+1,1)
exp=[1]
for i in range(length+1):
    print(str(round(100*i/(length+1)))+'% calculated')
    for j in range(length+1):
        if (((x[i])**power+y[j]**power)**(1/power))%1==0 and x[i]!=0 and y[j]!=0:
            plt.plot(x[i],y[j], 'ro')
            if x[i]==y[j]:#function e.g x[i]=y[i]
                if exp[-1]!=x[i]:
                    exp.append(x[i])
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
