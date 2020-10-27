import random
import ast
import numpy as np
#to make empty matrix



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

#save matrix to text file

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

#open matrix text file

def openmatrix(pretext,layers): 
    brain=[]
    for i in range(layers):
        f=open(str(pretext)+'Layer'+str(i)+'.txt','r')
        dat=f.readlines()
        data=[]
        for line in dat:
            data.append(ast.literal_eval(line))
        matrix=emptymatrix(len(data[0]),len(data))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                matrix[i,j]=data[i][j]
        brain.append(matrix)
    return brain
