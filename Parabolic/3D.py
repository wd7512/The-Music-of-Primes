import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
ran=10
fig = plt.figure()
ax = fig.gca(projection='3d')

x=np.arange(-ran,ran,.25)
z=np.arange(-ran,ran,.25)
j=np.sqrt(-1)
for i in range(len(z)):
    z[i]=z[i]*j
x, z=np.meshgrid(x,z)
y=np.sqrt((x+z)**4)
print(y)
surf = ax.plot_surface(x, z, y, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.xlabel('i')
plt.ylabel('i')
plt.show()
