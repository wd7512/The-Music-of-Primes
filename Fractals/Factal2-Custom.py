import turtle
import time
count=time.time()
times=[]
turtle.speed(speed=0)
length=200
angle=360/10
turtle.left(90)
def move(length,angle):
    turtle.forward(length)
    turtle.forward(-length)
    turtle.left(angle)
def startup(length,angle):
    for i in range(int(360/angle)):
        move(length,angle)
def tree(length,angle):
    turtle.forward(length*2)
    turtle.left(180-angle)
    for i in range(int(360/angle)-1):
        move(length,-angle)
    turtle.forward(length*2)
    turtle.left(180-angle)
startup(length,angle)

for i in range(int(360/angle)):    
    tree(length/2,angle)
for i in range(int(360/angle)): 
    turtle.forward(length)
    turtle.left(180-angle)
    for i in range(int(360/angle)-1):
        tree(length/4,angle)
    turtle.forward(length)
    turtle.left(180-angle)

for i in range(int(360/angle)):
    turtle.forward(length)
    turtle.left(180-angle)
    for i in range(int(360/angle)-1):
        turtle.forward(length/2)
        turtle.left(180-angle)
        for i in range(int(360/angle)-1):
            tree(length/8,angle)
        turtle.forward(length/2)
        turtle.left(180-angle)
    turtle.forward(length)
    turtle.left(180-angle)

for i in range(int(360/angle)):
    turtle.forward(length)
    turtle.left(180-angle)
    for i in range(int(360/angle)-1):
        turtle.forward(length/2)
        turtle.left(180-angle)
        for i in range(int(360/angle)-1):
            turtle.forward(length/4)
            turtle.left(180-angle)
            for i in range(int(360/angle)-1):
                tree(length/16,angle)
            turtle.forward(length/4)
            turtle.left(180-angle)
        turtle.forward(length/2)
        turtle.left(180-angle)
    turtle.forward(length)
    turtle.left(180-angle)
def maintree(length,angle,n):
    if n<1:
        return
    if n==1:   
        tree(length/2,angle)
        maintree(length,angle,n-1)
        
    
    
