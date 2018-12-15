import random
global deck

class setup():

    def newdeck():
        global deck
        deck=[]
        
        values=[2,3,4,5,6,7,8,9,10,11,12,13,14]
        suits=['D','S','C','H']
        
        for suit in suits:
            for value in values:
                deck.append([value,suit])
        
        deck=random.sample(deck,52) #shuffle deck

    def drawcard():
        global deck
        
        card=deck[0] #taking top card
        deck.remove(card)

        return card

    def deal(players):
        
        hands=[]
        
        for i in range(players): #first round of dealing
            hands.append([drawcard()])

        for i in range(players): #second round of dealing
            hands[i].append(drawcard())
        
        return hands

def playtable():

    table=[]

    #flop
    drawcard() #burning card
    table.append(drawcard())
    table.append(drawcard())
    table.append(drawcard())

    #turn
    drawcard() #buring card
    table.append(drawcard())

    #river
    drawcard() #buring card
    table.append(drawcard())

    return table






def play(players):
    
    newdeck()
    
    hands=deal(players)
    print('Hands:')
    for hand in hands:
        print(hand)

    table=playtable()
    print('Table:\n'+str(table))
    
