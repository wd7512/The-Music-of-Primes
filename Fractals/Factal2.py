import turtle
def tree(length):
    turtle.forward(length*2)
    move(length,90)
    move(length,90)
    turtle.left(90)
    move(length,90)
    turtle.left(90)
    turtle.left(90)
    turtle.forward(length*2)
    turtle.left(90)
def move(length,angle):
    turtle.forward(length)
    turtle.forward(-length)
    turtle.left(angle)
turtle.left(90)
move(100,90)
move(100,90)
move(100,90)
move(100,90)
tree(50)
tree(50)
tree(50)
tree(50)

#for i in range(10):
    #tree(100/(2**(i+1)))
