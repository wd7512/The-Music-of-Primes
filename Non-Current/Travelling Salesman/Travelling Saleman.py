import matplotlib.pyplot as plt
import random
import math
import time

def plotline(coords):
    xcor=[]
    ycor=[]
    for coord in coords:
        xcor.append(coord[0])
        ycor.append(coord[1])

    xcor.append(coords[0][0])
    ycor.append(coords[0][1])

    distance=0
    for i in range(len(coords)):
        x1=xcor[i]
        y1=ycor[i]
        x2=xcor[i+1]
        y2=ycor[i+1]
        distance=distance+math.sqrt((x2-x1)**2+(y2-y1)**2)

    plt.title('distance='+str(round(distance,2)))

    plt.plot(xcor,ycor,'--o')
    plt.plot(xcor[0],ycor[0],'ro')
    
    plt.show()
coords=[]
xcor=[]
ycor=[]
mean=[0,0]
for i in range(7):
    coords.append([random.randint(0,100),random.randint(0,100)])
    xcor.append(coords[i][0])
    ycor.append(coords[i][1])
    mean[0]=mean[0]+coords[i][0]
    mean[1]=mean[1]+coords[i][1]
mean[0]=mean[0]/7
mean[1]=mean[1]/7



plotline(coords)
#time.sleep(5)
plt.close()
