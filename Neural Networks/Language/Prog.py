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
        net1=emptymatrix(14,10*26) #10 chars
        net2=emptymatrix(2,14)
        for x in range(net1.shape[0]):
            for y in range(net1.shape[1]):
                net1[x,y]=random.randint(-100,100)
            
        for x in range(net2.shape[0]):
            for y in range(net2.shape[1]):
                net2[x,y]=random.randint(-100,100)
        
        brains.append([net1,net2])
    
    return brains

def savematrix(brain):
    count=0
    for sub in brain:
        print(sub)
        f=open('Layer'+str(count)+'.txt','w')
        save=[]
        for layer in sub:
            #print('L'+str(layer))
            save.append(str(layer))
        for i in range(len(save)):
            save[i]=save[i].split(' ')
       
        for s1 in save:
            #print(s1)
            s1=[x for x in s1
                if len(x)>0 and (str.isdigit(x[-1])==True
                                 or x[-2:]==']]')]
            #print(s1)

            #print(s1[0][0:2])
            
            if s1[0][0:2]=='[[':
                #print('bad')
                #print(s1[0][2:])
                s1[0]=s1[0][2:]

            #print(s1[-1][-2:])
            if s1[-1][-2:]==']]':
                #print('bad')
                #print(s1[0][2:])
                s1[-1]=s1[-1][:-2]
            
            f.write(str(s1)+'\n')
        f.close()
        count=count+1
        
            

