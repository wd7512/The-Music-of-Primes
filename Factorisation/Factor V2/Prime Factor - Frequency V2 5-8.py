import math
import matplotlib.pyplot as plt
import ast
global n
global y
f=open('Factors.txt', 'r')
y=ast.literal_eval(f.readline())
f.close()
n=int(input('How many numbers do you want to go up to?\n0 for max\nn:'))
if n==0:
    n=len(y)
def y1(r):
    y1=[0]
    for i in range(n):#numbers of r less than n
        if y[i]==r:
            y1.append(y1[i]+1)
        else:
            y1.append(y1[i])
    return(y1)
plt.plot(y1(5), label='5 Factors')
plt.plot(y1(6), label='6 Factors')
plt.plot(y1(7), label='7 Factors')
plt.plot(y1(8), label='8 Factors')
plt.legend()
plt.show()
