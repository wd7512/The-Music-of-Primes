import turtle
import time
count=time.time()
times=[]
turtle.speed(speed=0)
length=200
def move(length,angle):
    turtle.forward(length)
    turtle.forward(-length)
    turtle.left(angle)
def tree2(length):
    turtle.forward(length*2)
    move(length,90)
    move(length,90)
    turtle.left(90)
    move(length,90)
    turtle.left(90)
    turtle.left(90)
    turtle.forward(length*2)
    turtle.left(90)
def tree3(length):
    turtle.forward(length*4)
    turtle.left(90)
    tree2(length)
    tree2(length)
    tree2(length)
    turtle.forward(length*4)
    turtle.left(90)
def tree4(length):
    turtle.forward(length*8)
    turtle.left(90)
    tree3(length)
    tree3(length)
    tree3(length)
    turtle.forward(length*8)
    turtle.left(90)
def tree5(length):
    turtle.forward(length*16)
    turtle.left(90)
    tree4(length)
    tree4(length)
    tree4(length)
    turtle.forward(length*16)
    turtle.left(90)
def tree6(length):
    turtle.forward(length*32)
    turtle.left(90)
    tree5(length)
    tree5(length)
    tree5(length)
    turtle.forward(length*32)
    turtle.left(90)
def tree7(length):
    turtle.forward(length*64)
    turtle.left(90)
    tree6(length)
    tree6(length)
    tree6(length)
    turtle.forward(length*64)
    turtle.left(90)
def tree8(length):
    turtle.forward(length*128)
    turtle.left(90)
    tree7(length)
    tree7(length)
    tree7(length)
    turtle.forward(length*128)
    turtle.left(90)
def tree9(length):
    turtle.forward(length*256)
    turtle.left(90)
    tree8(length)
    tree8(length)
    tree8(length)
    turtle.forward(length*256)
    turtle.left(90)
move(length,90)
move(length,90)
move(length,90)
move(length,90)
turtle.left(90)
print(time.time()-count)
times.append(time.time()-count)
tree2(length/2)
tree2(length/2)
tree2(length/2)
tree2(length/2)
print(time.time()-count)
times.append(time.time()-count)
tree3(length/4)
tree3(length/4)
tree3(length/4)
tree3(length/4)
print(time.time()-count)
times.append(time.time()-count)
tree4(length/8)
tree4(length/8)
tree4(length/8)
tree4(length/8)
print(time.time()-count)
times.append(time.time()-count)
tree5(length/16)
tree5(length/16)
tree5(length/16)
tree5(length/16)
print(time.time()-count)
times.append(time.time()-count)
tree6(length/32)
tree6(length/32)
tree6(length/32)
tree6(length/32)
print(time.time()-count)
times.append(time.time()-count)
tree7(length/64)
tree7(length/64)
tree7(length/64)
tree7(length/64)
print(time.time()-count)
times.append(time.time()-count)
tree8(length/128)
tree8(length/128)
tree8(length/128)
tree8(length/128)
print(time.time()-count)
times.append(time.time()-count)
tree9(length/256)
tree9(length/256)
tree9(length/256)
tree9(length/256)
print(time.time()-count)
times.append(time.time()-count)
