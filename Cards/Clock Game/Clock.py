import random
global deck



def newdeck():
    global deck
    deck=[]
    
    values=[0,1,2,3,4,5,6,7,8,9,10,11,12] #cards shifted down by 1
    suits=['D','S','C','H']
    
    for suit in suits:
        for value in values:
            deck.append([value,suit])
    
    deck=random.sample(deck,52) #shuffle deck

def draw(): 
    global deck

    card=deck[0]
    deck.remove(card)

    return card

def dealclock():
    global deck
    clock=[]
    for i in range(12):
        clockarm=[]
        for i in range(4):
            clockarm.append(draw())
        clock.append(clockarm)

    return clock

def play():

    newdeck()
    clock=dealclock()
    middle=deck #last 4 remaining cards
    strikes=3 #number of cards in middle
    
    card=middle[0] #top card
    middle.remove(card) #take it away

    while strikes>0:
        #print(strikes)
        #print(card)
        if card[0]==12: #if king
            strikes=strikes-1

            card=middle[0] #top card
            middle.remove(card) #take it away
        else:
            num=card[0]
            #print(num)
            card=clock[num][0]
            #print(card)
            #print(clock[num])
            clock[num].remove(card)

    count=0
    for sets in clock: #counts how many empty sets
        if sets==[]:
            count=count+1

    if count==12: #if all sets empty
        return True
    else:
        return False
