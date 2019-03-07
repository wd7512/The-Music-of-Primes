import random
import matplotlib.pyplot as plt


def chance(odds):
    c=odds
    for i in range(odds):
        for j in range(odds):
            if (i+1)+(j+1)==odds and i!=j:
                c=c+1

    return 100*c/(odds**2)


odds=int(input('Odds out of:'))
print('Chance of Happening:'+str(chance(odds))+'%')

totest=[1,2,3,4,5,6,7,8,9,10,
        11,12,15,20,25,30,35,40,45,50]
x=[]
y=[]
for i in range(odds):
    x.append(i+1)
    y.append(chance(i+1))

print('Odds on - - - Percent Chance - - - Real odds')
for num in totest:
    if len(str(num))==1:
        pri='0'+str(num)
    else:
        pri=str(num)

    odo=chance(num)
    outof=100/odo
    outof=round(outof,2)
    odo=str(round(odo,3))
    
    while len(odo)>5:
        odo=odo[:-1]
    while len(odo)<5:
        odo=odo+'0'

    
    
    print(pri+'      - - - '+odo+'%         - - - 1/'+str(outof))


plt.xlabel('Odds on')
plt.ylabel('Percent Chance')
plt.plot(x,y)
plt.grid()
plt.show()
