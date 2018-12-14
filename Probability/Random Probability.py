import random
import matplotlib.pyplot as plt
num=int(input('How many times do you want to flip a coin?'))
lim=100
x=[1]
y=[random.randint(-lim,lim)]
for i in range(num-1):
    x.append(i+2)
    y.append(random.randint(-lim,lim)+y[i])
plt.plot(x,y)
plt.axis('equal')
plt.show()
