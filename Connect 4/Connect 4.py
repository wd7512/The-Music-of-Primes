#connect 4
import numpy as np
import random
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

def run_ai_vs_human(brain):
    game = newgame()
    w,b = brain

    turn = int(input('Human First press 1, Ai first press 2'))


    
    while check_four(game) == False:
        print(game)
        
        
        if turn == 1:
            col = int(input('p'+str(turn)+' column:'))
            if np.any(addchip(turn,col,game)) == False:
                print('player 2 wins')
                return 
            turn = 2
        else:
            proba = run_brain(w,b,game)
            col = np.argmax(proba)
            count = 0
            while np.any(addchip(turn,col,game)) == False:
                proba[0,np.argmax(proba)] = -100
                col = np.argmax(proba)
                if count > 6:
                    return 0
                count = count + 1
                
            
            turn = 1
            

        

    if turn == 1:
        turn = 2
    else:
        turn = 1
    print('player '+str(turn)+' wins')
    print(game)

def input_convert(gam):
    return gam.resize((1,84))


def random_matricies():
    sizes = (84,50,7)
    weight_sizes = [(a,b) for a,b in zip(sizes[:-1],sizes[1:])]
    weights = [np.random.standard_normal(s) for s in weight_sizes]
    #print(weights)
    biases = [np.random.standard_normal((1,s)) for s in sizes[1:]]
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

    #TEMP
    #weights,biases = random_matricies()
    
    inputs = game_conv(game)
    input_convert(inputs)

    layer1 = function(np.matmul(inputs,weights[0])+biases[0]) #shape (1,50)

    #layer2 = function(np.matmul(layer1,weights[1])+biases[1])

    output = function(np.matmul(layer1,weights[1])+biases[1])
    
    return output
    
#a=newgame()
#addchip(1,1,a)
#addchip(2,2,a)
def run_ai(brain1,brain2,game):
    game = newgame()
    w1,b1 = brain1
    w2,b2 = brain2

    turn = 1

    while check_four(game) == False:
        #print(str(game)+'\n')
        #col = int(input('p'+str(turn)+' column:'))
        
        if turn == 1:
            proba = run_brain(w1,b1,game)
            col = np.argmax(proba)
            count = 0
            while np.any(addchip(turn,col,game)) == False:
                proba[0,np.argmax(proba)] = -100
                col = np.argmax(proba)
                if count > 6:
                    return 0
                count = count + 1
                
            
            turn = 2
        else:
            proba = run_brain(w2,b2,game)
            col = np.argmax(proba)
            
            while np.any(addchip(turn,col,game)) == False:
                proba[0,np.argmax(proba)] = -100
                col = np.argmax(proba)
                count = 0
                if count > 6:
                    return 0
                count = count + 1
            turn = 1

    if turn == 1:
        turn = 2
    else:
        turn = 1
    #print('player '+str(turn)+' wins')
    #print(game)

    return turn

def init_gens():
    gens = []
    for i in range(1000):
        gens.append(random_matricies())

    return gens

def test_ai(gens):
    wins = []
    num = len(gens)
    for i in range(num):
        wins.append(0)
        
    for i in range(num):
        for j in range(num):
            if i != j:
                result = run_ai(gens[i],gens[j],newgame())
                if result == 0:
                    wins[i] = wins[i] + 0.5
                    wins[j] = wins[j] + 0.5
                if result == 1:
                    wins[i] = wins[i] + 1
                if result == 2:
                    wins[j] = wins[j] + 1
                
                

    return wins

def evolve(wina,gens):
    wins = wina[:]
    new_gens = []
    for i in range(200):
        new_gens.append(random_matricies())

    survivors = []
    for i in range(40):
        top = wins.index(max(wins))
        survivors.append(gens[top])
        new_gens.append(gens[top])
        wins[top] = -1

    for brain in survivors:
        for i in range(19):
            new_gens.append(mutate(brain))
            

    return new_gens



def mutate(brain):
    add1 = random_matricies()
    add2 = []
    for matrix in add1:
        subadd = []
        for mat in matrix:
            if random.randint(0,100) == 50:
                subadd.append(mat/50)
            else:
                subadd.append(0)
        add2.append(subadd)

    for i in range(2):
        for j in range(2):
            brain[i][j] = brain[i][j] + add2[i][j]
            
    return brain

def learning(gens,runs):
    wins = test_ai(gens)
    for i in range(runs):
        gens = evolve(wins,gens)
        wins = test_ai(gens)
        print(str(max(wins))+' '+str(sum(wins[:200])/200)+' '+str(sum(wins[-800:-760])/50)+' '+str(sum(wins[-760:])/750))

    return gens,wins


gens = init_gens()
for i in range(100):
    print('Gen '+str(i))
    gens,wins = learning(gens,1)
    

