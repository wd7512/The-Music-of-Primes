import ast
import numpy as np
global fmatrix

numfiles=int(input('How many files?:'))


def newmatrix():
    global fmatrix
    empty='0 0'
    for i in range(168): #169 different hands
        empty=empty+';0 0'
    fmatrix=np.matrix(empty) #makes empty 2 coloumn matrix

    #print(fmatrix)
    
    values=['02','03','04','05',
            '06','07','08','09',
            '10','11','12','13',
            '14']

    for value in values: #make first coloumn matrix


def cardconvert(value):

    var=int(value)
    
    if var<11: #if not royal / ace
        return value
    else:
        if var==11:
            return 'J'
        if var==12:
            return 'Q'
        if var==13:
            return 'K'
        if var==14:
            return 'A'

    

for i in range(numfiles):
    f=open('2people'+str(i+1)+'.txt','r')
    

    
    lines=f.readlines()
    for line in lines:
        line=ast.literal_eval(line)
    
