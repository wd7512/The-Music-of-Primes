import random
import matplotlib.pyplot as plt
import math



def fast_bet(val,bet_col):
    num = random.randint(0,14)
    if num == 0: 
        col = 0 #green
    elif num in list(range(1,8)): 
        col = 1 #red
    else:
        col = 2 #black

    #print(col)

    if col == bet_col:
        if col == 0:
            out = val * 14
        else:
            out = val * 2
    else:
        out = - val

    return out


def child_strat():
    
    total_bal = 5000
    children = 8

    risk_of_loss = 1 / 2**3
    
    init_bet = math.floor(total_bal * risk_of_loss / children)
    init_bal = math.floor(total_bal / children)
    
    children_bets = [init_bet for i in range(children)]
    children_bals = [init_bal for i in range(children)]

    max_rounds = 10000
    round_count = 0
    end = False

    graph = [total_bal]

    while end == False:
        round_count = round_count + 1
        
        if round_count > max_rounds:
            end = True

        
        for i in range(children):
            


            add = fast_bet(children_bets[i],1)
            children_bals[i] = children_bals[i] - add

            

            total_bal = sum(children_bals)

            if children_bals[i] < 0:
                
                if total_bal < 0:
                    end = True

                children_bals = [total_bal / children for i in range(children)]
                #children_bets[i] = math.floor(total_bal * risk_of_loss / children)
                children_bets = children_bets = [math.floor(total_bal * risk_of_loss / children) for i in range(children)]

            else:
                if add > 0:
                    pass
                else:
                    children_bets[i] = children_bets[i] * 2


            graph.append(total_bal)

    plt.plot(graph)
    plt.show()


    return [round_count,total_bal,children_bets,children_bals]
                
child_strat()
            
    
    
