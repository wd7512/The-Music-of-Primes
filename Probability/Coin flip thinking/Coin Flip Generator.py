import random
import matplotlib.pyplot as plt
num=int(input('How many times do you want to flip a coin?'))
runs=int(input('How many runs'))
def draw(num):

    x1=[1]
    y1=[0]
    for i in range(num-1):
        x1.append(i+2)
        y1.append((random.randint(0,1))*2-1+y1[i])

    maxx=abs(y1[0])
    for numm in y1:
        if abs(numm)>maxx:
            maxx=numm
    index=y1.index(maxx)
    #print('max on first line - ('+str(index)+','+str(maxx)+')')

    x2=[y1.index(maxx)+1]
    y2=[maxx]
    for i in range(num-1-index):
        x2.append(i+2+y1.index(maxx))
        y2.append((random.randint(0,1))*2-1+y2[i])

    y3=y1[index:]

    if len(y3)>len(y1)/3:
        avg1=sum(y3)/len(y3)
        avg2=sum(y2)/len(y2)
        print('original avg : '+str(avg1))
        print('shifted avg : '+str(avg2))

        f=open(str(num)+'flips cut.txt','a')
        f.write(str([avg1,avg2])+'\n')
        f.close()
        
    '''
    #print(y2)
    plt.plot(x1,y1,label='original')
    plt.plot(x2,y2,label='shifted')
    plt.axis('equal')
    plt.legend()
    plt.show()
    '''
    
for i in range(runs):
    draw(num)
