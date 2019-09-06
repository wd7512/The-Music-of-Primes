#connect 4
import numpy as np
def newgame():

    return np.zeros([6,7],dtype=int)

def addchip(playernum,col,game):
    #col is column ranging 0-6

    if game[0,col] != 0:
        return False

    placed = False
    for i in range(6):
        if game[5-i,col] == 0 and placed == False:
            game[5-i,col] = playernum
            placed = True
        
    return game

def check_four(game):
    
    
    for i in range(6): #horizontal
        line = game[i]
        for j in range(4):
            if line[j] != 0 and all(x == line[j] for x in line[j:j+4]) == True:
                return line[j]

    for i in range(7):
        line = [game[0][i],game[1][i],game[2][i],game[3][i],game[4][i],game[5][i]]
        for j in range(3):
            if line[j] != 0 and all(x == line[j] for x in line[j:j+4]) == True:
                return line[j]

    for i in range(3):
        for j in range(4):
            line = [game[i][j],game[i+1][j+1],game[i+2][j+2],game[i+3][j+3]]
            if line[0] != 0 and all(x == line[0] for x in line) == True:
                return line[0]

    for i in range(3):
        for j in range(4):
            line = [game[i+3][j],game[i+2][j+1],game[i+1][j+2],game[i][j+3]]
            if line[0] != 0 and all(x == line[0] for x in line) == True:
                return line[0]

    return False

def run_human():
    game = newgame()

    turn = 1
    
    while check_four(game) == False:
        print(game)
        col = int(input('p'+str(turn)+' column:'))
        addchip(turn,col,game)
        if turn == 1:
            turn = 2
        else:
            turn = 1

    if turn == 1:
        turn = 2
    else:
        turn = 1
    print('player '+str(turn)+' wins')
    print(game)

def input_convert(game):
    return game.resize((1,42))
def input_revert(game):
    return game.resize((6,7))
