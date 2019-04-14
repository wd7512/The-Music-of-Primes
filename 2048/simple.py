import random

def newboard(size):
    board=[]
    line=[]
    for i in range(size):
        line.append(0)
    for i in range(size):
        board.append(line)
    return board

def draw(board):
    for line in board:
        print(line)
    
def rounds(board):
    
    count=-1
    for line in board:
        for num in line:
            if num==0:
                count=count+1
    if count<0:
        return False
    else:
        ran=random.randint(0,count)
        print(ran)
        size=len(board)
        for i in range(size):
            for j in range(size):
                if ((i*size)+j)==ran:
                    print(i)
                    print(j)
                    board[i][j]=1
        return board
a=newboard(3)
