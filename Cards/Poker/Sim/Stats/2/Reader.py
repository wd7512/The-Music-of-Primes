import ast
import numpy as np
global fmatrix

#numfile=int(input('Index of File?:'))


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

    cone=[]
    for i in range(13):
        for j in range(13-i):
            cone.append(values[i]+values[j+i])
    print(cone)
    print(len(cone))
        


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

    


#f=open('2people'+str(numfile)+'.txt','r')
    

    
#lines=f.readlines()
#for line in lines:
    #line=ast.literal_eval(line)
    
