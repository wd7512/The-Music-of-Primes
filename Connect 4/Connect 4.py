#connect 4
import numpy as np
def newgame():

    return np.zeros((6,7),dtype=int)

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

def input_convert(gam):
    return gam.resize((84,1))


def random_matricies():
    sizes = (84,50,50,7)
    weight_sizes = [(a,b) for a,b in zip(sizes[1:],sizes[:-1])]
    weights = [np.random.standard_normal(s) for s in weight_sizes]
    #print(weights)
    biases = [np.random.standard_normal((s,1)) for s in sizes]
    #print(biases)

    return [weights,biases]

def function(x):
    return 1/(1+np.exp(-x))

def game_conv(game):
    p = np.zeros((12,7),dtype=int)

    for i in range(6):
        for j in range(7):
            if game[i][j] == 1:
                p[i][j] = 1
            if game[i][j] == 2:
                p[i+6][j] = 1

    return p

def run_brain(weights,biases,game):
    
    inputs = game_conv(game)
    input_convert(inputs)
    return inputs
    
