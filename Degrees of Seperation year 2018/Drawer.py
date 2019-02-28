import turtle
import os
import math
import random
files=os.listdir()
for filename in files:
    if (filename[-3:])!='txt':
        files.remove(filename)
print(files)
mainnodes=[]
for filename in files:
    f=open(filename,'r')
    contents=f.readlines()
    if contents!=[]:
        mainnodes.append(filename)
    f.close()

nosubnodes=len(files)
nomainnodes=len(mainnodes)
print(str(nosubnodes)+' nodes')
print(str(nomainnodes)+' mainnodes')

radius=380
pen=turtle.Turtle()
pen.speed(10000000)
pen.ht()
#pen.penup()
#pen.setpos(0,-radius)
#pen.pendown()
#pen.circle(radius)
angle=2*math.pi/nosubnodes

points=[]

coords=[]
minirad=10
for i in range(nosubnodes):
    points.append(0)
    pen.penup()

    if files[i] in mainnodes:
        pen.color('blue')
        x=math.sin(angle*i)*(radius)
        y=math.cos(angle*i)*(radius)
    else:
        pen.color('orange')
        x=math.sin(angle*i)*radius
        y=math.cos(angle*i)*radius
    
    
    #x=random.randint(-radius,radius)
    #y=random.randint(-radius,radius)
    
    coords.append([x,y])
    pen.setpos(x,y-minirad)
    pen.pendown()
    
    
    
    
    pen.circle(minirad)


pen.color('Black')
for node in mainnodes:
    pos=coords[files.index(node)]
    
    f=open(node,'r')
    names=f.readlines()
    for name in names:
        name=name[0:-1]+'.txt'
        index=files.index(name)
        moveto=coords[index]


        pen.penup()
        pen.setpos(pos[0],pos[1])
        pen.pendown()
        pen.setpos(moveto[0],moveto[1])

        points[coords.index(pos)]=points[coords.index(pos)]+1
        points[coords.index(moveto)]=points[coords.index(moveto)]+1
        
    f.close()
    
for i in range(nosubnodes):
    points[i]=[points[i],files[i]]


