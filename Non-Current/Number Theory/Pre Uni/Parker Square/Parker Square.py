# parker square
import random
import math

def emptysquare(sides):
    square=[]
    line=[]

    for i in range(sides):
        line.append(0)
    for i in range(sides):
        square.append(line)

    return square

def evolve(square,variance):
    size=len(square)

    for i in range(size):
        for j in range(size):
            keep=random.randint(0,1) #chance of changing
            #keep=0
            if keep==0:
                a=random.randint(-variance+1,variance)
                #print(a)
                square[i][j]=square[i][j]+a
    return square

def randomsquare(sides):
    square=[]
    

    for i in range(sides):
        line=[]
        for i in range(sides):
            
            line.append(random.randint(1,15))
                        
        square.append(line)

    return square

def check(square):
    
    check=[]
    size=len(square)
    
    for i in range(size): #col
        total=0
        for row in square:
            total=total+row[i]
        #print('col'+str(i+1)+':  '+str(total))
        check.append(total)

    for i in range(size):
        total=sum(square[i])

        #print('row'+str(i+1)+':  '+str(total))
        check.append(total)


    diag1=0
    diag2=0
    for i in range(size):
        diag1=diag1+square[size-i-1][i]
        diag2=diag2+square[i][i]

    #print('diag1:  '+str(diag1))
    check.append(diag1)
    #print('diag2:  '+str(diag2))
    check.append(diag2)

    similars=[]
    for i in range(len(check)):
        count=0
        for j in range(len(check)):
            if check[i]==check[j]:
                count=count+1
    similars.append(count)

    return (max(similars))
            
def train(sides,pop,generations):

    if generations==0:
        generations=99999999999


    squares=[]
    for i in range(pop):
        squares.append(randomsquare(sides))

    scores=[]
    for square in squares:
        scores.append(check(square))

    wins=[]

    for score in scores:
        if score==8:
            wins.append(squares[scores.index(score)])

    if len(wins)>0:
        return wins

    bestscore=max(scores)
    bestsquare=squares[scores.index(bestscore)]

    #end of setup

    for i in range(generations):
        print('generation'+str(i+1))
        
        squares=[]
        for i in range(pop):
            #print(8-bestscore)
            new=evolve(bestsquare,8-bestscore)
            print('new'+str(new)) #whats going on here
            squares.append(new)
            print(squares)

        
        
        scores=[]
        for square in squares:
            scores.append(check(square))

        wins=[]

        for score in scores:
            if score==8:
                wins.append(squares[scores.index(score)])

        if len(wins)>0:
            return wins

        bestscore=max(scores)
        bestsquare=squares[scores.index(bestscore)]

        #print(squares)
        #print(scores)
        
        print(bestscore)
        print(bestsquare)
