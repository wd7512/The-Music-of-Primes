import math
import matplotlib.pyplot as plt
n=int(input('Gauss Estimate of how many primes, graph up to\nn:'))
def g(z):
        a=2
        b=0
        while a!=z:
                b=b+1/math.log(a)#Log Function
                a=a+1
        return(b)
x=[]
for i in range(n):
        x.append(i)
y=[0,0]
for i in range(n-2):
        y.append(g(2+i))
plt.plot(x, y)
plt.xlabel('Total Numbers')
plt.ylabel('Number of Primes')
plt.show()
