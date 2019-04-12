import random
import matplotlib.pyplot as plt

def mean(lis):
    num=0
    for a in lis:
        num=num+a
    return num/len(lis)
def xcheck(point,grad,xlis,ylis):
    xcount=0
    for i in range(100):
        x=xlis[i]
        y=ylis[i]
        newy=point[1]+grad*(x-point[0])
        xcount=(y-newy)**2+xcount
    return xcount

x=[]
y=[]
for i in range(100):
    num=random.randint(0,100)
    x.append(num)
    if random.randint(0,2)==0:
        y.append(2*num+random.randint(-50,50))
    else:
        y.append(2*num+random.randint(-12,12))
print('x-'+str(mean(x)))
print('y-'+str(mean(y)))
fac=0.1
grad=1
for i in range(100):
    if (i+1)%10==0:
        fac=fac/10
    che=xcheck([mean(x),mean(y)],grad,x,y)
    #print(che)
    print(grad)
    if xcheck([mean(x),mean(y)],grad+grad*fac,x,y)<che:
        grad=grad+grad*fac
    if xcheck([mean(x),mean(y)],grad-grad*fac,x,y)<che:
        grad=grad-grad*fac

x1=[]
for i in range(101):
    x1.append(i)
y1=[]
for num in x1:
    y1.append(mean(y)+grad*(num-mean(x)))
plt.plot(x,y,'o')
plt.plot(x1,y1)
plt.show()
