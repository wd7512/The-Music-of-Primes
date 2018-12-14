global cards
import random
global deck

def shuff():
    value=['2','3','4','5','6','7','8','9','90','91','92','93','94']
    suit=['d','h','c','s']
    deck=[]

    for a in suit:
        for b in value:
            deck.append(b+a)
            #print(b+a)
    #print(deck)
    #print(a)
    return (random.sample(deck,len(deck)))

def draw(burn):
    global deck
    if burn==True:
        print('card burnt')
        return
    card=deck[0]#take top card
    deck.remove(card)
    print('card drawn')
    return card

def ontable():
    table=[]
    #end of pre-flop
    draw(True)
    table.append(draw(False))
    table.append(draw(False))
    table.append(draw(False))
    print('Flop: '+str(table))
    #end of flop
    draw(True)
    table.append(draw(False))
    print('Turn: '+str(table))
    #end of turn
    draw(True)
    table.append(draw(False))
    print('River: '+str(table))
    #end of river
    return table





deck=shuff()
print(deck)
hands=[]
table=[]
score=[]
players=3
for i in range(players):
    hands.append([])
        

for i in range(2):
    for a in hands:
        a.append(draw(False))#all draw
print('All hands:\n'+str(hands))

table=ontable()
#cards=hands[0]+table
cards=['4a','2a','3a','7a','5a','6a','8a']
var1=[cards[0]]#1st card
var2=[cards[1]]#2nd card
var3=[cards[2]]#1st table card
num1=0

