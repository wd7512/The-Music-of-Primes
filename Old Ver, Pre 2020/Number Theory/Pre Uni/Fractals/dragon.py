import turtle
import math
import numpy as np

clock=np.matrix('1 1;-1 1')/math.sqrt(2)
anticlock=np.matrix('1 -1;1 1')/math.sqrt(2)

def draw(coords):
    pen.penup()
    pen.setpos(coords[0])
    pen.pendown()
    for pos in coords:
        pen.setpos(pos)

def update(coords):
    new=[]
    count1=0
    count2=0
    for i in range(len(coords)-1):
        x3=0
        y3=0
        new.append(coords[i])
        x1,y1=coords[i]
        x2,y2=coords[i+1]
        leng=math.sqrt((x2-x1)**2+(y2-y1)**2)/2

        if math.log(len(coords)-1,2)%2==0:
            if abs(x1-x2)<0.01:
                y3=(y1+y2)/2
                if (i+1)%1==0:
                    x3=x1-leng
                else:
                    x3=x1+leng
                count1=count1+1

            elif abs(y1-y2)<0.01:
                x3=(x1+x2)/2
                if (i+1)%2==1:
                    y3=y1-leng
                else:
                    y3=y1+leng
                count2=count2+1
        else:
            if abs(x1-x2)<0.01:
                y3=(y1+y2)/2
                if (i+1)%1==0:
                    x3=x1+leng
                else:
                    x3=x1-leng
                count1=count1+1

            elif abs(y1-y2)<0.01:
                x3=(x1+x2)/2
                if (i+1)%2==1:
                    y3=y1+leng
                else:
                    y3=y1-leng
                count2=count2+1

        
        new.append([round(x3,8),round(y3,8)])

    new.append(coords[-1])
    #print(new)
    return new

def rotate(coords,mat):
    new=[]
    for pos in coords:
        a=mat*[[pos[0]],[pos[1]]]
        new.append([round(float(a[0][0]),8),round(float(a[1][0]),8)])
    #print(new)
    return new


pen=turtle.Turtle()
pen.speed(1000)
coords=[[-200,200],[0,0],[200,200]]
coords=rotate(coords,clock)
draw(coords)
pen.clear()

for i in range(100):
    coords=update(coords)
    if (i+1)%2==1:
        coords=rotate(coords,clock)
    else:
        coords=rotate(coords,anticlock)
    draw(coords)
    nxt=input('o')
    pen.clear()
