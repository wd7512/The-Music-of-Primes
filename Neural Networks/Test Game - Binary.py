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
        inp=converter(key)
        output=inp*brain
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
        brains.append(randommatrix(-100,100,16,4))
    test=[]
    for i in range(rounds):
        test.append(random.randint(0,15))
    halfbrains=learn(brains,popsize,rounds,test,1)
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
            test.append(random.randint(0,15))
        halfbrains=learn(newbrains,popsize,rounds,test,i)
        bestscore=play(test,halfbrains[0])
        print(bestscore)
        xgen.append(i)
        yscore.append(bestscore)
        i=i+1

    savematrix(halfbrains[0],'binary1')

    plt.plot(xgen,yscore)
    plt.show()
    
    return i

        
    
        
def learn(brains,popsize,rounds,test,gen):
    scores=[]
    
    for i in range(popsize):
        
        score=play(test,brains[i])
        scores.append([score*100,i+1])
    #print(scores)
    print(max(scores))
    #print(scores)
    live=[]
    for score in scores:
        if random.randint(0,int(gen))<score[0]:
            live.append(score)

    #print(live)
    live=sorted(live,reverse=True)
    livebrains=[]
    for life in live:
        #print(life)
        livebrains.append(brains[life[1]-1])
    #print(livebrains)
    #print(len(livebrains))
    while len(livebrains)!=popsize/4: #takes top %
        if len(livebrains)<popsize/4:
            livebrains.append(randommatrix(-100,100,16,4))
        else:
            livebrains=livebrains[0:len(livebrains)-1]
    return livebrains

def evolve(halfbrains):
    index=int(len(halfbrains)/10)
    brains=halfbrains[:]
    for i in range(4):
        for j in range(index):
            for k in range(3*(4-i)): #increased pop to maintain
                add=randommatrix(-5,5,16,4)
                brains.append(add+brains[i*index+j])

    return brains

start(2000,100)
