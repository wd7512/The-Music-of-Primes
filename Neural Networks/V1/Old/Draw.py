import turtle
import random

MT = turtle.Turtle()
MT.speed(100)
MT.penup()

inputs=['position','top','top-right','right','bottom-right','bottom',
        'bottom left','left','top-left']

outputs=['1 / on','0 / off']

inputpos=[]
for i in range(9):
    inputpos.append([-300,200-50*i])
middlepos=[]
for i in range(5):
    middlepos.append([0,200-100*i])
outputpos=[]
for i in range(2):
    outputpos.append([300,100-200*i])

for i in range(9):
    MT.setposition(inputpos[i])
    MT.pendown()
    MT.circle(20)
    MT.penup()
    MT.setposition(inputpos[i][0]-100,inputpos[i][1]+10)
    MT.pendown()
    MT.write(inputs[i])
    MT.penup()

for i in range(5):
    MT.setposition(middlepos[i])
    MT.pendown()
    MT.circle(20)
    MT.penup()

for i in range(2):
    MT.setposition(outputpos[i])
    MT.pendown()
    MT.circle(20)
    MT.penup()
    MT.setposition(outputpos[i][0]+50,outputpos[i][1]+10)
    MT.pendown()
    MT.write(outputs[i])
    MT.penup()

for i in range(9):
    for j in range(5):
        MT.penup()
        MT.setposition(inputpos[i][0]+20,inputpos[i][1]+20)
        MT.pendown()

        MT.setposition(middlepos[j][0]-20,middlepos[j][1]+20)

for i in range(5):
    for j in range(2):
        MT.penup()
        MT.setposition(middlepos[i][0]+20,middlepos[i][1]+20)
        MT.pendown()
        MT.setposition(outputpos[j][0]-20,outputpos[j][1]+20)

    
#turtle.getscreen()._root.mainloop()
