import ast
import numpy as np
global matrix

numfile=input('Index of File?:')


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
                matrix.append([values[i]+values[j+i]+'s',0,0,0,0]) #makes list of all combinations
            matrix.append([values[i]+values[j+i],0,0,0,0])

    #matrix in form [cards,%wins,no.wins,no.loss,no.draw]
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

    

    
def formats(hand):

    handstr1=hand[0][0]+hand[1][0] #make 4 char index
    handstr2=hand[1][0]+hand[0][0]
    
    if hand[0][1]==hand[1][1]: #if suited
        handstr1=handstr1+'s' #add suited
        handstr2=handstr2+'s' #add suited
    
    return [handstr1,handstr2]

def analyse(numfile):
    global matrix
    newmatrix()

    f=open('2people'+str(numfile)+'.txt','r')
    lines=f.readlines()
    for line in lines:
        line=ast.literal_eval(line)

        #print(line)
        if line[0]=='win': #if win
            winhand=formats(line[1][0])
            losshand=formats(line[3][0])

            #print(hand)

            
            
            for com in matrix:
                #print(com)
                if com[0] in winhand:
                    com[2]=com[2]+1
                if com[0] in losshand:
                    com[3]=com[3]+1

        else: #if draw
            print('draw')

    #print(matrix)
    for sets in matrix:
        sets[1]=round(100*sets[2]/(sets[2]+sets[3]),2)
    for i in range(169):
        for j in range(168):
            var1=matrix[j][:]
            var2=matrix[j+1][:]
            if var1[1]<var2[1]:
                matrix[j]=var2
                matrix[j+1]=var1

    #for sets in matrix:
        #print(sets)

    f=open('2people'+str(numfile)+'-analysed.txt','a')
    f.write('HAND-WIN%-TOTALWINS-TOTALLOSS-TOTALDRAWS\n')
    for sets in matrix:
        f.write(str(sets)+'\n')

    f.close()
    return

#analyse(numfile)
for i in range(39):
    analyse(i+31)
            
    
