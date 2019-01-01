import random
global deck



def newdeck():
    global deck
    deck=[]
    
    values=[2,3,4,5,6,7,8,9,10,11,12,13,14]
    suits=['D','S','C','H']
    
    for suit in suits:
        for value in values:
            deck.append([value,suit])
    
    deck=random.sample(deck,52) #shuffle deck

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

def drawcard():
        global deck
        
        card=deck[0] #taking top card
        deck.remove(card)

        return card

class check:

    # index of how hands are ranked
    '''
    straight flush = 1
    4 of a kind = 2
    full house = 3
    flush = 4
    straight = 5
    3 of a kind = 6
    2 pair = 7
    1 pair = 8
    nothing/high card = 9
    '''
    # in the form [rank,cards]
    
    def flush(hand,table):

        cards=hand+table
        flush=[]
        
        for card in cards: #for all cards
            if hand[0][1]==card[1]: #if suited to first hand card
                flush.append(card)
                
        #print(flush)

        if len(flush)<5: #if flush is not make with first hand card use second
            flush=[]
            for card in cards:
                if hand[1][1]==card[1]:
                    flush.append(card)

        if len(flush)<5: #if flush not made with hand at all, check table
            flush=[]
            for card in cards:
                if table[0][1]==card[1]:
                    flush.append(card)

        while len(flush)>5: #make sure highest possible
            flush.remove(min(flush))

        
        if len(flush)==5: #if flush
            flush=sorted(flush,reverse=True) #order flush high to low
            return [4,flush]
        else:
            return False

    def anysamenum(repeats):
        for card1 in repeats:
            for card2 in repeats:
                if card1[0]==card2[0] and card1!=card2:
                    return False #checks every card against eachother for repeats
        return True

    def connect(cards):
        for i in range(4):
            if cards[i][0]-cards[i+1][0]!=1: #if any of the cards dont connect
                return False
        return True
    
    def straight(hand,table):

        cards=hand+table
        straight=[]

        #print('in straight'+str(cards))
        
        cards=sorted(cards,reverse=True) #sort cards high to low

        repeats=[]

        for card1 in cards:
            for card2 in cards:
                if card1[0]==card2[0] and card1!=card2:
                    repeats.append(card2) #checks every card against eachother and adds repeats to a list
                    
        #print(repeats)

        i=0 #counter
        while check.anysamenum(repeats)==False: #while there are still repeats
            if repeats[i+1][0]==repeats[i][0]:
                repeats.remove(repeats[i+1]) #remove them
            i=i+1
            
        for card in repeats:
            cards.remove(card)

        #print(cards)

        if len(cards)<5: #if not enough cards to make straight
            return False

        #we now have at least 5 different cards that could make a straight
        
        if len(cards)==5 and check.connect(cards)==True: #if connected
            return [5,cards]

        if len(cards)==6:
            if check.connect(cards[0:5])==True:
                return [5,cards[0:5]]
            if check.connect(cards[1:6])==True:
                return [5,cards[1:6]]

        if len(cards)==7:
            if check.connect(cards[0:5])==True:
                return [5,cards[0:5]]
            if check.connect(cards[1:6])==True:
                return [5,cards[1:6]]
            if check.connect(cards[2:7])==True:
                return [5,cards[2:7]]
        
        return False

    def similarend(rank,similar,cards):
        for card in similar: #remove cards already being outputted
            cards.remove(card)

        cards=sorted(cards, reverse=True) 
        
        while len(cards+similar)>5:
            cards.remove(cards[-1]) #take of the lowest cards to leave highest kickers

        return [rank,similar+cards]

    def similar(hand,table):

        cards=hand+table
        similar=[]

        for card1 in cards:
            for card2 in cards:
                if card1[0]==card2[0] and card1!=card2: #if same as another card
                    #print(card1)
                    similar.append(card1)

        similar=sorted(similar, reverse=True)

        #print(similar)
        
        if len(similar)==2: #if only a pair
            return check.similarend(8,similar,cards)

        
        if len(similar)==4: #if two pair
            return check.similarend(7,similar,cards)

        if len(similar)==6: #either 3 of a kind or 3 pairs
            if similar[0][0]==similar[2][0]:# 3 of a kind
                for i in range(3):
                    similar.remove(similar[1+i]) #remove duplicates

                return check.similarend(6,similar,cards)

            else: #3 pairs
                
                similar.remove(similar[-1])
                similar.remove(similar[-1]) #remove lowest pair

                return check.similarend(7,similar,cards)
            

        if len(similar)==8: #full house


            if similar[0][0]!=similar[2][0]: #if pair is before 3 of a kind

                similar=similar[2:9]+similar[0:2]

                #print(similar)
            
            for i in range(3):
                similar.remove(similar[1+i]) #remove duplicates

            return [3,similar]


        if len(similar)==12: #4 of a kind

            for i in range(4):
                similar.remove(similar[1+i])
                similar.remove(similar[1+i]) #remove duplicates
            
            return check.similarend(2,similar,cards)

        else: #if nothing is made
            cards=sorted(cards, reverse=True)
            while len(cards)>5:
                cards.remove(cards[-1])
            return [9,cards]

def result(hand,table):

    results=[]
    cards=hand+table

    straighthand=check.straight(hand,table)
    flushhand=check.flush(hand,table)
    similarhand=check.similar(hand,table)

    #print(straighthand)
    #print(flushhand)
    #print(similarhand)

    if straighthand!=False:
        results.append(straighthand)
    if flushhand!=False:
        results.append(flushhand)
    if similarhand!=False:
        results.append(similarhand)

        
    if straighthand!=False and flushhand!=False: #if flush and straights are made

        suit=flushhand[1][0][1] #gets suit of flush
        #print(suit)

        for card in cards:
            if card[1]!=suit:
                cards.remove(card) #removing non suited cards

        cards=sorted(cards, reverse=True) #order cards
        #print(cards)
        
        if check.connect(cards)!=False: #if flush is also straight
            return [1,cards]

    result=min(results)
    
    return result

def convert(num):
    if num==1:
        return 'Straight-Flush'
    if num==2:
        return '4 of a Kind'
    if num==3:
        return 'Full House'
    if num==4:
        return 'Flush'
    if num==5:
        return 'Straight'
    if num==6:
        return '3 of a Kind'
    if num==7:
        return '2 Pairs'
    if num==8:
        return 'Pair'
    if num==9:
        return 'High Card'


def play(players):
    
    newdeck() #generates new deck
    
    hands=deal(players) #deals players
    
    print('Hands:')
    for hand in hands:
        print(hand) #displays hands

    table=playtable()
    print('\nTable:\n'+str(table)+'\n') #deals table and shows

    winner=[]

    for hand in hands:
        winner.append(result(hand,table)) #tests hands

    winningcards=min(winner) #takes best hand
    
    player=winner.index(winningcards) #finds which players it is

    winningcards[0]=convert(winningcards[0])

    print('player '+str(player)+' wins\nwith a hand of '+str(hands[player])+'\nand cards:\n'+str(winningcards))
    