import random
import matplotlib.pyplot as plt
num=int(input('How many times do you want to flip a coin?'))
x=[1]
y=[random.randint(0,1)]
for i in range(num-1):
    x.append(i+2)
    y.append(random.randint(0,1)+y[i])
plt.plot(x,y)
plt.axis('equal')
plt.show()
