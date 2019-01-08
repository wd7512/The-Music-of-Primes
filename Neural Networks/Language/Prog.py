#26*23 max word = 598 input vector
import numpy as np
import random

alphabet=['A','B','C','D','E',
          'F','G','H','I','J',
          'K','L','M','N','O',
          'P','Q','R','S','T',
          'U','V','W','X','Y',
          'Z']
def start():
    f=open('Reading.txt','r')
    linesread=f.readline()
    print(linesread)
    linesread=int(linesread[12:])
    print(linesread)
    
    f.close()

    return linesread
def save(brain,linesread):
    linesread=start()
    f=open('Reading.txt','w')
    f.write('LINES READ: '+str(linesread)+'\n')
    f.write('\n'+str(brain[0])+'\n\n'+str(brain[1]))
    f.close()
    
def emptymatrix(x,y):
    a=''
    for i in range(x):
        a=a+'0 '
    b=''
    for i in range(y-1):
        b=b+a+';'
    b=b+a

    return np.matrix(b)

def randombrain(population):
    

    brains=[]

    for i in range(population):
        net1=emptymatrix(14,10)
        net2=emptymatrix(2,14)
        for x in range(net1.shape[0]):
            for y in range(net1.shape[1]):
                net1[x,y]=random.randint(-100,100)
            
        for x in range(net2.shape[0]):
            for y in range(net2.shape[1]):
                net2[x,y]=random.randint(-100,100)
        
        brains.append([net1,net2])
    
    return brains
