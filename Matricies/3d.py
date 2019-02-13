import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
'''
Primitive Pythagorean quadruples
1 2 2 3
2 10 11 15
4 13 16 21
2 10 25 27

35 70 70 105
14 70 77 105
20 65 80 105


'''
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
#theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#z = np.linspace(-2, 2, 100)
#r = z**2 + 1
#x = r * np.sin(theta)
#y = r * np.cos(theta)

unitcube=np.array([[0,1,1,1,0,0,0,1],
                   [0,0,1,1,1,0,1,0],
                   [0,0,0,1,1,1,0,1]])
unitcube=np.asmatrix(unitcube)

mat=np.matrix(

ax.plot(unitcube[0],unitcube[1],unitcube[2],'o')

plt.show()
