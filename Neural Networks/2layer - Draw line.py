#2 layers
#connections, top row is input 1, bottom row input 2
import numpy as np
import random

def cleanmatrix(size):
    #size=int(input('Size of Matrix'))
    empty=''
    line=''
    for i in range(size):
        line=line+'0 '
    empty=empty+line
    for i in range(size-1):
        empty=empty+';'+line
    return np.matrix(empty)
def score(matrix): #at least 3x3 and same dimensions
    score=0
    for i in range(len(matrix)-2): #not checking edges
        for j in range(len(matrix)-2): #not checking edges
            self=matrix[i+1,j+1]

            if matrix[i,j+1]==self: #top
                score=score-1
            if matrix[i,j+2]==self: #top right
                score=score+1
            if matrix[i+1,j+2]==self: #right
                score=score-1
            if matrix[i+2,j+2]==self: #right bottom
                score=score+1
            if matrix[i+2,j+1]==self: #bottom
                score=score-1
            if matrix[i+2,j]==self: #bottom left
                score=score+1
            if matrix[i+1,j]==self: #left
                score=score-1
            if matrix[i,j]==self: #left top
                score=score+1

    return score

def draw(brain,size):
    matrix=cleanmatrix(size)

    for i in range(size):
        for i in range(size-2):
            for j in range(size-2):
                inputs=np.matrix('0 0 0 0 0 0 0 0 0')
                
                inputs[0,0]=matrix[i+1,j+1] #itself
                
                inputs[0,1]=matrix[i,j+1] #top
                inputs[0,2]=matrix[i,j+2] #top right
                inputs[0,3]=matrix[i+1,j+2] #right
                inputs[0,4]=matrix[i+2,j+2] #bottom right
                inputs[0,5]=matrix[i+2,j+1] #bottom
                inputs[0,6]=matrix[i+2,j] #bottom left
                inputs[0,7]=matrix[i+1,j] #left
                inputs[0,8]=matrix[i,j] #left top            
            
                outputs=inputs*brain
                #print(outputs)
                if outputs[0,0]>outputs[0,1]: #if 1st>2nd
                    matrix[i+1,j+1]=1
                if outputs[0,1]>outputs[0,0]: #if 2nd>1st
                    matrix[i+1,j+1]=0
                if outputs[0,0]==outputs[0,1]: #if same do random
                    matrix[i+1,j+1]=random.randint(0,1)

    return matrix



def randomminds(numberofbrains): #randomly assign connections
    brains=[]
    for i in range(numberofbrains):
        brain=np.matrix('0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0')
        for i in range(9):
            for j in range(2):
                brain[i,j]=random.randint(-100,100) #as percentage
        brains.append(brain)

    return brains
            
def evolve(numberofbrains,brain):
    #print('population size'+str(numberofbrains))
    brains=[brain]
    change=random.randint(0,100)
    extras=0
    
    if change<6: #extra random mutations
        extras=round((numberofbrains-1)/(change+2))
        ranbrains=randomminds(extras)
        for ranbrain in ranbrains:
            brains.append(ranbrain)
        print(str(extras)+' have randomly mutated')
        
    for i in range(numberofbrains-1-extras):
        add=np.matrix('0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0')
        for i in range(9):
            for j in range(2):
                add[i,j]=random.randint(-5,5)
        brains.append(brain+add)

    for brain in brains:
        for i in range(9):
            for j in range(2):
                if brain[i,j]>100:
                    brain[i,j]=100
                if brain[i,j]<-100:
                    brain[i,j]=-100
    return brains

def play(rounds,popsize):
    brains=randomminds(popsize)
    for i in range(rounds):
        scores=[]
        for brain in brains:
            scores.append(score(draw(brain,10)))
        best=brains[scores.index(max(scores))]
        print(draw(best,10))
        print(max(scores))
        print(str(best)+'\n==========')
        brains=evolve(popsize,best)
    
