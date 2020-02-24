import matplotlib.pyplot as plt
lim=int(input('Up to what positive integer?'))
x=[]
for i in range(lim+1):
    x.append(((i)**2))
print(x)
plt.plot(x)
plt.show()
