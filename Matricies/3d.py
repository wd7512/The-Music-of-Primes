import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math


def invlist(lis):
    new=[]
    for i in range(len(lis)):
        new.append(-lis[i])
    return new

'''
np.asmatrix - to matrix
np.asarray - to array
Primitive Pythagorean quadruples
1 2 2 3
2 10 11 15
4 13 16 21
2 10 25 27

35 70 70 105
14 70 77 105
20 65 80 105


'''

    


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
'''
print(unitcube)
'''
size=105
xcir=[]
ycir=[]
zcir=[]
for xx in range(size+1):
    #print(xx)
    for yy in range(size+1):
        for zz in range(size+1):
            if math.sqrt(xx**2+yy**2+zz**2)==5:
                xcir.append(xx)
                ycir.append(yy)
                zcir.append(zz)


xfull=[]
yfull=[]
zfull=[]

for i in range(3):
    for j in range(8):
        if i==0:
            if unitcube[i,j]==1:
                xfull=xfull+invlist(xcir)
            else:
                xfull=xfull+xcir
        if i==1:
            if unitcube[i,j]==1:
                yfull=yfull+invlist(ycir)
            else:
                yfull=yfull+ycir
        if i==2:
            if unitcube[i,j]==1:
                zfull=zfull+invlist(zcir)
            else:
                zfull=zfull+zcir

ax.plot(xfull,yfull,zfull,'bo')


circle=np.array([xfull,yfull,zfull])

for i in range(circle.shape[1]):
    ax.plot([0,circle[0,i]],[0,circle[1,i]],[0,circle[2,i]],color='black')

mat=np.array([[4,0,0],
              [0,2,0],
              [0,0,2]])

new=np.asarray(np.asmatrix(mat)*np.asmatrix(circle))

#ax.plot(unitcube[0],unitcube[1],unitcube[2],'ro')



ax.plot(new[0],new[1],new[2],'go')

d=25
for i in range(new.shape[1]):
    mx=new[0,i]
    my=new[1,i]
    mz=new[2,i]


    nx=math.sqrt(d/(1+(my**2+mz**2)/mx**2))
    if mx<0:
        nx=-nx
    ny=nx*my/mx
    nz=nx*my/mx

    #ax.plot([],[],[],colour='blue')
    ax.plot([nx,mx],[ny,my],[nz,mz],color='green')

ax.axis('equal')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


plt.show()
