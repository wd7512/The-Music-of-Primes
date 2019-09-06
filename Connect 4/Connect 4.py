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
    print('checks if 4')
