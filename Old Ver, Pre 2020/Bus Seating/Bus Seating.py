import ast
import turtle
file='Classic 72 - 12.3.19.txt'
f=open(file,'r')
data=f.readlines()
f.close()
for i in range(len(data)):
    if data[i]!='\n':
        data[i]=ast.literal_eval(data[i])
for line in data:
    print(line)

size=20
pen=turtle.Turtle()
pen.speed(10000)
for i in range(len(data)):
    pen.penup()
    pen.goto(-5*size,(10-2*i)*size)
    
    
    if data[i]!='\n':
        
        for i in range(len(data[i])):
            pen.pendown()
            pen.circle(size)
            pen.penup()
            pen.forward(2*size)

for a in range(40):
    a=a+1
    for i in range(len(data)):
        if data[i]!='\n':
            for k in range(5):
                if data[i][k]==a:
                    nxt=input('Next:')
                    pen.penup()
                    pen.goto((2*k-5)*size,(10-2*i)*size)
                    pen.pendown()
                    pen.color('red')
                    pen.circle(size/2)
                    
