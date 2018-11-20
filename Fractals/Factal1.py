import turtle
turtle.speed(speed=10)
def tree(length,n):
    if length>0:
        turtle.left(69)
    turtle.forward(length)

    if n%2==0:
        tree(-length,n+1)
    tree(length/(1), n+1)
    
    
    return
tree(200,2)
