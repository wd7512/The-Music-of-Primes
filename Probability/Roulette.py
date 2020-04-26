import random
import matplotlib.pyplot as plt

def bet(val,bet_col):
    num = random.randint(0,14)
    if num == 0:
        col = 'GREEN'
    elif num in list(range(1,8)):
        col = 'RED'
    else:
        col = 'BLACK'

    #print(col)

    if col == bet_col:
        if col == 'GREEN':
            out = val * 14
        else:
            out = val * 2
    else:
        out = - val

    return out

def fast_bet(val,bet_col):
    num = random.randint(0,14)
    if num == 0:
        col = 0
    elif num in list(range(1,8)):
        col = 1
    else:
        col = 2

    #print(col)

    if col == bet_col:
        if col == 0:
            out = val * 14
        else:
            out = val * 2
    else:
        out = - val

    return out

def strat_1():
    bal = [2**6]

    bet_val = 1

    end = False
    while end == False:
        add = fast_bet(bet_val,1)
        bal.append(bal[-1] + add)
        if add < 0:
            bet_val = bet_val * 2
        else:
            bet_val = 1

        if bal[-1] < 0:
            end = True

    #plt.plot(bal)
    #plt.show()

    return bal

def ana_1():
    
    runs = 20
    lengths = []
    maxes = []

    for i in range(runs):
        a = strat_1()
        lengths.append(len(a))
        maxes.append(max(a))


    return [lengths,maxes]

a = ana_1()
