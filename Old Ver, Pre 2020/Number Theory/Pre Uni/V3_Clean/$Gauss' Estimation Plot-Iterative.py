import math
import matplotlib.pyplot as plt
n=int(input('Gauss Estimate of how many primes, graph up to\nn:'))
def k(x):
        return(1/math.log(x))
x=[]
for i in range(n):
        x.append(i)

q=[0,0]
for i in range(n-2):
        q.append(q[i+1]+1/math.log(i+2))
plt.plot(x, q)
plt.xlabel('Total Numbers')
plt.ylabel('Number of Primes')
plt.show()
