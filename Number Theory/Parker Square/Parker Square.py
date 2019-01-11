# parker square

def emptysquare(sides):
    square=[]
    line=[]

    for i in range(sides):
        line.append(0)
    for i in range(sides):
        square.append(line)

    return square

def check(square):
    
    check=[]
    
    for i in range(len(square)): #col
        total=0
        for row in square:
            total=total+row[i]
        print('col'+str(i+1)+':  '+str(total))
        check.append(total)

    for i in range(len(square)):
        total=sum(square[i])

        print('row'+str(i+1)+':  '+str(total))
        check.append(total)


    diag1=0
    diag2=0
    for i in range(len(square)):
        diag1=diag1+square[len(square)-i-1][i]
        diag2=diag2+square[i][i]

    print('diag1:  '+str(diag1))
    check.append(diag1)
    print('diag2:  '+str(diag2))
    check.append(diag2)

    

    
    
