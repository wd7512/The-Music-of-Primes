import ast
import numpy as np
global matrix

numfile=int(input('Index of File?:'))


def newmatrix():
    global matrix
    
    values=['02','03','04','05',
            '06','07','08','09',
            '10','11','12','13',
            '14']

    matrix=[]
    for i in range(13):
        for j in range(13-i):
            if j!=0:
                matrix.append([values[i]+values[j+i]+'s',0,0]) #makes list of all combinations
            matrix.append([values[i]+values[j+i],0,0])
    #print(matrix)

    #print(len(matrix))

    

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

    
newmatrix()

f=open('2people'+str(numfile)+'.txt','r')
    

    
lines=f.readlines()
for line in lines:
    line=ast.literal_eval(line)

    #print(line)
    if line[0]=='win': #if win
        hand=line[1][0]

        #print(hand)

        for card in hand:
            if card[0]=='01':
                card[0]='14'
        handstr=hand[0][0]+hand[1][0]

        if hand[0][1]==hand[1][1]: #if suited
            handstr=handstr+'s'
        
        for com in matrix:
            if com[0]==handstr:
                com[1]=com[1]+1

    else: #if draw
        print('draw')

print(matrix)
for i in range(169):
    for j in range(168):
        var1=matrix[j][:]
        var2=matrix[j+1][:]
        if var1[1]<var2[1]:
            matrix[j]=var2
            matrix[j+1]=var1

for sets in matrix:
    print(sets)
            
    
