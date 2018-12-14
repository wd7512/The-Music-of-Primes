global cards
import random
global deck

def shuff():
    value=['2','3','4','5','6','7','8','9','90','91','92','93','94']
    #90=ten
    #91=jack
    #92=queen
    #93=king
    #94=ace
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

def flush(cards):
    #print(cards)
    var1=[cards[0]]#1st card
    var2=[cards[1]]#2nd card
    var3=[cards[2]]#1st table card
    for i in range(6):
        #print(cards[i+1][1])
        if cards[0][-1]==cards[i+1][-1]:#other cards suited to first
            var1.append(cards[i+1])
    if len(var1)<3:
        for i in range(5):
            if cards[1][-1]==cards[i+2][-1]:#other cards suited to second
                var2.append(cards[i+2])
    if len(var1)+len(var2)<4:
        for i in range(4):
            if cards[2][-1]==cards[i+3][-1]:#other cards suited to second
                var3.append(cards[i+3])
    print('var1'+str(var1))
    print('var2'+str(var2))
    print('var3'+str(var3))
    if len(var1)>4:
        while len(var1)!=5:
            var1.remove(min(var1))
        return var1#return flush cards
    if len(var2)>4:
        while len(var2)!=5:
            var2.remove(min(var2))
        return var2#return flush cards
    if len(var3)>4:
        while len(var3)!=5:
            var3.remove(min(var3))
        return var3#return flush cards
    return False

def straight(cards):
    var1=[cards[0]]#1st card
    var2=[cards[1]]#2nd card
    print(sorted(cards))

def result(hand,table):
    test=hand+table
    print(test)
    fl=flush(test)
    st='straight'
    fk='4kind'
    fh='fullhouse'
    tk='3kind'
    
    print(fl)
    if fl!=False:#flush?
        if st!=False:#straight?
            [1,'HAND']#add hand
        score=[4,fl]
        print(score)

        
    return


def run():
    global deck
    deck=shuff()
    print(deck)
    hands=[]
    table=[]
    score=[]
    players=int(input('number of players: '))
    for i in range(players):
        hands.append([])
        

    for i in range(2):
        for a in hands:
            a.append(draw(False))#all draw
    print('All hands:\n'+str(hands))

    table=ontable()
    
    #for a in hands:
        #score.append(result(a,table))
run()
