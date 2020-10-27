import numpy as np

def emptymatrix(x,y): #makes empty matrix
    a=''
    for i in range(x):
        a=a+'0 '
    b=''
    for i in range(y-1):
        b=b+a+';'
    b=b+a

    return np.matrix(b)

def randombrain(population): #random networks of 2 layers

    brains=[]

    inputsize=16
    hiddensize=14
    outputsize=4

    for i in range(population):
        net1=emptymatrix(hiddensize,inputsize) #16 inputs
        net2=emptymatrix(outputsize,hiddensize) #4 outputs
        for x in range(net1.shape[0]):
            for y in range(net1.shape[1]):
                net1[x,y]=random.randint(-100,100)
            
        for x in range(net2.shape[0]):
            for y in range(net2.shape[1]):
                net2[x,y]=random.randint(-100,100)
        
        brains.append([net1,net2])
    
    return brains

def savematrix(brain,generation): #saves in good form
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
