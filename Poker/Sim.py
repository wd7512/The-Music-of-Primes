global cards
import random
global deck

def shuff():
    value=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
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
    card=deck[random.randint(0,len(deck)-1)]
    deck.remove(card)
    print('card drawn')
    return card

def ontable():
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

def result(hand,table):
    winningplayer=0#0 to number of players-1
    test=hand+table
    print(test)
    if flush(test)!=False:
        print(max(flush(test)))
    return

def flush(cards):
    var1=[cards[0]]
    var2=[cards[1]]
    for i in range(len(cards)-1):
        if cards[0][1]==cards[i+1][1]:
            var1.append(cards[i+1])
    if len(var1)<3:
        for i in range(len(cards)-2):
            if cards[1][1]==cards[i+2][1]:
                var2.append(cards[i+2])
    if len(var1)==5:
        return var1
    if len(var2)==5:
        return var2
    return False
deck=shuff()
print(deck)
hands=[]
table=[]
players=int(input('number of players: '))
for i in range(players):
    hands.append([])
    

for i in range(2):
    for a in hands:
        a.append(draw(False))#all draw
print('All hands:\n'+str(hands))

table=ontable()

for a in hands:
    result(a,table)
