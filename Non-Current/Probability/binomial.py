import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

p=float(input('p(0-1):'))
n=int(input('n:'))

def factorial(x):
    y=1
    for i in range(x):
        y=y*(i+1)
    return y

def comb(n,r):

    return int(factorial(n)/(factorial(r)*factorial(n-r)))

def power(x,n):
    y=x+0
    for i in range(n):
        y=y*x

    return y


x=[]
y=[]
for i in range(n+1):
    x.append(i)
    y.append(comb(n,i)*power(p,i)*power(1-p,n-i))

plt.bar(x,y)
plt.show()
