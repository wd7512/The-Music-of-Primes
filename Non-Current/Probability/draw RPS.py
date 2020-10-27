import matplotlib.pyplot as plt
import numpy as np
import random

def emptymatrix(x,y): #makes empty matrix
    a=''
    for i in range(x):
        a=a+'0 '
    b=''
    for i in range(y-1):
        b=b+a+';'
    b=b+a

    return np.matrix(b)

data=emptymatrix(100,100)
'''
0=nothing
1=rock
2=paper
3=scissors
'''

def check(mid,other):

    if mid==0: #if mid empty
        return other
    
    if other==0: #if other empty
        return mid

    if mid==other:
        return other

    if mid==1:
        if other==2: #rock-paper
            return other
        if other==3: #rock-scissors
            return mid

    if mid==2:
        if other==1: #paper-rock
            return mid
        if other==3: #paper-scissors
            return other

    if mid==3:
        if other==1: #scissors-rock
            return other
        if other==2: #scissors-paper
            return mid
    

def update(data):
    size=data.shape[0]


    for i in range(int((size)/2)-1): #excluding border
        i=i+1
        for j in range(int((size/2)-1)): #excluding border
            j=j+1
            #data[2*i,2*j]=4
            
            mid=data[2*i,2*j]
            top=data[2*i-1,2*j]
            right=data[2*i,2*j+1]
            bot=data[2*i+1,2*j]
            left=data[2*i,2*j-1]

            data[2*i-1,2*j]=check(mid, top)
            data[2*i,2*j+1]=check(mid, right)
            data[2*i+1,2*j]=check(mid, bot)
            data[2*i,2*j-1]=check(mid, left)
            

    for i in range(int((size)/2)-1): #excluding border
        for j in range(int((size/2)-1)): #excluding border
            #data[2*i+1,2*j+1]=4
            
            mid=data[2*i+1,2*j+1]
            top=data[2*i,2*j+1]
            right=data[2*i+1,2*j+2]
            bot=data[2*i+2,2*j+1]
            left=data[2*i+1,2*j]

            data[2*i,2*j+1]=check(mid, top)
            data[2*i+1,2*j+2]=check(mid, right)
            data[2*i+2,2*j+1]=check(mid, bot)
            data[2*i+1,2*j]=check(mid, left)

    return data

a=emptymatrix(50,50)
for i in range(10):
    a[random.randint(1,49),random.randint(1,49)]=1
    a[random.randint(1,49),random.randint(1,49)]=2
    a[random.randint(1,49),random.randint(1,49)]=3

while True:
    a=update(a)
    plt.imshow(a)
    plt.show()
    plt.clf
