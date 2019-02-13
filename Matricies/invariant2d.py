import numpy as np
import matplotlib.pyplot as plt
import math

def sizecheck(mat):
    for i in range(mat.shape[1]):
        while math.sqrt(mat[0,i]**2+mat[1,i]**2)<35:
            mat[0,i]=mat[0,i]*2
            mat[1,i]=mat[1,i]*2
    return mat



def circ(x,radius):
    #print('work')
    y=[]
    for i in range(x.shape[0]):
        y.append(math.sqrt(radius**2-x[i]**2))
    return y
def circinv(x,radius):
    #print('work')
    y=[]
    for i in range(x.shape[0]):
        y.append(-math.sqrt(radius**2-x[i]**2))
    return y

#sqa=np.array([[0,1,1,0],[0,0,1,1]])
#sqm=np.asmatrix(sqa)
mata=np.array([[1,1],[2,4]])
matm=np.asmatrix(mata)

circle00=[0,7,15,20,24,25,24,20,15,7]
circle0=circle00[:]
for num in circle00: #fix
    #print(num)
    circle0.append(-num)
circle1=circle0[int(len(circle0)/4):]+circle0[0:int(len(circle0)/4)]
#print([circle0,circle1])
cira=np.array([circle0,circle1])

#cira=np.array([[0,3,4,5,4,3,0,-3,-4,-5,-4,-3],
               #[5,4,3,0,-3,-4,-5,-4,-3,0,3,4]])
cirm=np.asmatrix(cira)



new=matm*cirm
new=sizecheck(new)
print(new)

#plt.plot(sqm[0],sqm[1],'bo')
plt.plot(new[0],new[1],'ro')
plt.plot(cira[0],cira[1],'bo')

x=np.arange(-25,25,0.001)
plt.plot(x,circ(x,25),'blue')
plt.plot(x,circinv(x,25),'blue')

x=np.arange(-35,35,0.0001)
plt.plot(x,circ(x,35),'green')
plt.plot(x,circinv(x,35),'green')


for i in range(cira.shape[1]):
    plt.plot([0,cirm[0,i]],[0,cirm[1,i]],'black')
    
    grad=new[1,i]/new[0,i]
    x=math.sqrt(35*35/(1+grad**2))
    if new[0,i]<0:
        x=-x
    y=grad*x
    plt.plot(x,y,'go')

    plt.plot([cirm[0,i],x],[cirm[1,i],y],'black')
    
    plt.plot([x,new[0,i]],[y,new[1,i]],'black')




plt.axis('equal')
plt.grid()

plt.show()

