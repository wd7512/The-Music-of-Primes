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

def play(test,brain):
    score=0
    for key in test:
        inp=emptymatrix(4,1)
        inp[0,key-1]=1
        output=inp*brain
        #print(key)
        
        maxx=output[0,0]
        for i in range(output.shape[1]):
            if output[0,i]>maxx:
                output[0,i]=maxx
        for i in range(output.shape[1]):
            if output[0,i]==maxx:
                num=i+1
        #print(output)
        #print(num)
                
        if num==key:
            #print('YEs')
            score=score+1
    return score/len(test)
    
def start(popsize,rounds):
    brains=[]
    for i in range(popsize):
        brains.append(randommatrix(-100,100,4,4))
    test=[]
    for i in range(rounds):
        test.append(random.randint(1,4))
    halfbrains=learn(brains,popsize,rounds,test)
    i=1
    bestscore=0
    xgen=[]
    yscore=[]
    while bestscore!=1:
        print('GEN ==== '+str(i))
        #print(len(halfbrains))
        
        newbrains=evolve(halfbrains)
        #print(len(newbrains))
        test=[]
        for j in range(rounds):
            test.append(random.randint(1,4))
        halfbrains=learn(newbrains,popsize,rounds,test)
        bestscore=play(test,halfbrains[0])
        print(bestscore)
        xgen.append(i)
        yscore.append(bestscore)
        i=i+1

    plt.plot(xgen,yscore)
    plt.show()
    
    return i

        
    
        
def learn(brains,popsize,rounds,test):
    scores=[]
    
    for i in range(popsize):
        
        score=play(test,brains[i])
        scores.append([score*100,i+1])
    print(max(scores))
    #print(scores)
    live=[]
    for score in scores:
        if random.randint(0,100)<score[0]:
            live.append(score)

    #print(live)
    live=sorted(live,reverse=True)
    livebrains=[]
    for life in live:
        #print(life)
        livebrains.append(brains[life[1]-1])
    #print(livebrains)
    #print(len(livebrains))
    while len(livebrains)!=popsize/4: #takes top 25%
        if len(livebrains)<popsize/4:
            livebrains.append(randommatrix(-100,100,4,4))
        else:
            livebrains=livebrains[0:len(livebrains)-1]
    return livebrains

def evolve(halfbrains):
    index=int(len(halfbrains)/10)
    brains=halfbrains[:]
    for i in range(4):
        for j in range(index):
            for k in range(3*(4-i)): #increased pop by 300% to maintain
                add=randommatrix(-6,6,4,4)
                brains.append(add+brains[i*index+j])

    return brains
