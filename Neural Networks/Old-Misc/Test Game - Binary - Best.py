import random
import ast
import numpy as np
import matplotlib.pyplot as plt


def emptymatrix(x,y):
    a=''
    for i in range(x):
        a=a+'0 '
    b=''
    for i in range(y-1):
        b=b+a+';'
    b=b+a
    return np.matrix(b)

#to make random matrix

def randommatrix(low,high,x,y):
    matrix=emptymatrix(x,y)
    for i in range(y):
        for j in range(x):
            matrix[i,j]=random.randint(low,high)
    return matrix

def converter(num):
    output=emptymatrix(4,1)
    if num==0:
        return output
    if num%2!=0:
        output[0,3]=1
    if num>13:
        output[0,0]=1
        output[0,1]=1
        output[0,2]=1
        return output
    if num>11:
        output[0,0]=1
        output[0,1]=1
        return output
    if num>9:
        output[0,0]=1
        output[0,2]=1
        return output
    if num>7:
        output[0,0]=1
        return output
    if num>5:
        output[0,1]=1
        output[0,2]=1
        return output
    if num>3:
        output[0,1]=1
        return output
    if num>1:
        output[0,2]=1
        return output
    return output

def savematrix(matrix,pretext): 
    count=0
    for sub in matrix:
        print(sub)
        f=open(str(pretext)+'Layer'+str(count)+'.txt','w')
        save=[]
        for layer in sub:
            save.append(str(layer))
        for i in range(len(save)):
            save[i]=save[i].split(' ')
       
        for s1 in save:
            s1=[x for x in s1
                if len(x)>0 and (str.isdigit(x[-1])==True
                                 or x[-2:]==']]')]
            if s1[0][0:2]=='[[':
                s1[0]=s1[0][2:]
            if s1[-1][-2:]==']]':
                s1[-1]=s1[-1][:-2]
            f.write(str(s1)+'\n')
        f.close()
        print('saved')
        count=count+1
    

def play(test,brain):
    score=0
    for key in test:
        #print(brain)
        inp=converter(key)
        #print(brain[0])
        mid=inp*brain[0]
        output=(mid)*brain[1]
        #print(key)
        
        maxx=output[0,0]
        for i in range(output.shape[1]):
            if output[0,i]>maxx:
                output[0,i]=maxx
        for i in range(output.shape[1]):
            if output[0,i]==maxx:
                num=i
        #print(output)
        #print(num)
                
        if num==key:
            #print('YEs')
            score=score+1
    return score/len(test)
    
def start(popsize,rounds):
    brains=[]
    for i in range(popsize):
        
        brains.append([randommatrix(-100,100,8,4),randommatrix(-100,100,16,8)])
    test=[]
    for i in range(rounds):
        test.append(random.randint(0,15))
    bestbrain=learn(brains,popsize,rounds,test,1)
    i=1
    bestscore=0
    xgen=[]
    yscore=[]
    while bestscore!=1:
        print('GEN ==== '+str(i))
        
        newbrains=evolve(bestbrain)
        #print(len(newbrains))
        test=[]
        for j in range(rounds):
            test.append(random.randint(0,15))
        bestbrain=learn(newbrains,popsize,rounds,test,i)
        bestscore=play(test,bestbrain)
        print(bestscore)
        xgen.append(i)
        yscore.append(bestscore)
        i=i+1

    savematrix(bestbrain,'binary1')

    plt.plot(xgen,yscore)
    plt.show()
    
    return i

        
    
        
def learn(brains,popsize,rounds,test,gen):
    scores=[]
    
    for i in range(popsize):
        
        score=play(test,brains[i])
        scores.append([score*100,i])
    

    scores=sorted(scores,reverse=True)

    #print(scores)

    return brains[scores[0][1]]
'''
def evolve(bestbrain,pop):
    brains=[]
    brains.append(bestbrain)


    for i in range(int(pop*9/10-1)):
        brain=[]
        
        add=randommatrix(-4,4,8,4)
        brain.append(bestbrain[0]+add)

        add=randommatrix(-4,4,16,8)
        brain.append(bestbrain[1]+add)

        brains.append(brain)

        
    for i in range(int(pop/10)):
        brains.append([randommatrix(-100,100,8,4),randommatrix(-100,100,16,8)])

    #print(len(brains))

    return brains
'''
def evolve(halfbrains):
    index=int(len(halfbrains)/10)
    brains=halfbrains[:]
    print(brains)
    for i in range(4):
        for j in range(index):
            for k in range(3*(4-i)): #increased pop to maintain
                add1=randommatrix(-5,5,16,8)
                add2=randommatrix(-5,5,8,4)
                brains.append([add1+brains[i*index+j][0],add2+brains[i*index+j][1]])

    print(brains)
    return brains
start(100,100)
