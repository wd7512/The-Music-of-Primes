import matplotlib.pyplot as plt
import math

def check(a,b):
    seta=[a]
    setb=[b]
    for i in range(round(math.sqrt(a))+1):
        if a%(i+2)==0:
            seta.append(i+2)
    for i in range(round(math.sqrt(b))+1):
        if b%(i+2)==0:
            setb.append(i+2)
    for num in seta:
        if num in setb:
            return False

    return True

length=40

for x1 in range(length-1):
    for y1 in range(length-1):
        if check(x1+2,y1+2)==True and x1!=y1:
            plt.plot(x1+2,y1+2,'ro')
plt.axis('Equal')
plt.show()
