#26*23 max word = 598 input vector
import numpy as np
import random
import ast

alphabet=['A','B','C','D','E',
          'F','G','H','I','J',
          'K','L','M','N','O',
          'P','Q','R','S','T',
          'U','V','W','X','Y',
          'Z']

    
def emptymatrix(x,y): #makes empty matrix
    a=''
    for i in range(x):
        a=a+'0 '
    b=''
    for i in range(y-1):
        b=b+a+';'
    b=b+a

    return np.matrix(b)

def randombrain(population): #random networks
    # 2 layers 260-14-2
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

def savematrix(brain,generation):
    count=0
    for sub in brain:
        print(sub)
        f=open(str(generation)+'Layer'+str(count)+'.txt','w')
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
        
def openmatrix(generation,layers): #number of generations already done and layers of network

    brain=[]
    for i in range(layers): #for each layer
        
        f=open(str(generation)+'Layer'+str(i)+'.txt','r')
        dat=f.readlines()


        data=[]

        for line in dat:
            data.append(ast.literal_eval(line))

       
        
        #print(data)

        matrix=emptymatrix(len(data[0]),len(data))

        #print(matrix)
            

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                #print(i)
                #print(j)
                matrix[i,j]=data[i][j]

        brain.append(matrix)
    return brain

def evolve(numberofbrains,brain):
    #print('population size'+str(numberofbrains))
    brains=[brain]
    change=random.randint(0,100)
    extras=0
    
    if change<6: #extra random mutations
        extras=round((numberofbrains-1)/(change+2))
        ranbrains=randombrain(extras)
        for ranbrain in ranbrains:
            brains.append(ranbrain)
        print(str(extras)+' have randomly mutated')

        
    for i in range(numberofbrains-1-extras):
        add1=emptymatrix(14,260)
        for i in range(260):
            for j in range(14):
                add1[i,j]=random.randint(-5,5)
        add2=emptymatrix(2,14)
        for i in range(14):
            for j in range(2):
                add2[i,j]=random.randint(-3,3)
                
        brains.append([brain[0]+add1,brain[1]+add2])

    for brain in brains:
        for subbrain in brain:
            for i in range(subbrain.shape[0]):
                for j in range(subbrain.shape[1]):
                    if subbrain[i,j]>100:
                        subbrain[i,j]=100
                    if subbrain[i,j]<-100:
                        subbrain[i,j]=-100
    return brains

def score(brain):
    True
    #work here

def start(currentgen,uptogen,pop):
    bestbrain=openmatrix(currentgen,2)
    brains=evolve(pop,bestbrain)

    for i in range(uptogen-currentgen):
        scores=[]
        

        for brain in brains:
            scores.append(score(brain))
    #print(brains)
    
    
    
