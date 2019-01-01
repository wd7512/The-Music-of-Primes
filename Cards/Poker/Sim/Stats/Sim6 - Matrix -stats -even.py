import random
import numpy as np


global deck

def newdeck():
    global deck
    deck=[]

    values=['02','03','04','05',
            '06','07','08','09',
            '10','11','12','13',
            '14']
    suits=['H','C','S','D']

    for suit in suits:
        for value in values:
            deck.append([value,suit])

    deck=random.sample(deck,52)

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

class check:

    # index of how hands are ranked
    '''
    straight flush = 9
    4 of a kind = 8
    full house = 7
    flush = 6
    straight = 5
    3 of a kind = 4
    2 pair = 3
    1 pair = 2
    nothing/high card = 1
    '''
    # in the form [rank,cards]

    def flush(hand,table):

        cards=hand+table
        flush=[]
        
        for card in cards: #for all cards
            if hand[0][1]==card[1]: #if suited to first hand card
                flush.append(card)
                
        #print(flush)

        if len(flush)<5: #if flush is not made with first hand card use second
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
            #print(str([6,flush]))
            flush=sorted(flush,reverse=True) #order flush high to low
            return [6,flush]
        else:
            return False

    def connect(cards):
        for i in range(4):
            if int(cards[i][0])-int(cards[i+1][0])!=1: #if any of the cards dont connect
                return False
        return True

    def wrapstraight(hand,table): #checking wrap

        cards=hand+table
        straight=[]

        for card in cards:
            if card[0]=='14':
                card[0]='01' #conver ace to one

        #print('in straight'+str(cards))
        
        cards=sorted(cards,reverse=True) #sort cards high to low

        #print(cards)

        repeats=[]

        for card1 in cards:
            for card2 in cards:
                if card1[0]==card2[0] and card1!=card2:
                    repeats.append(card2) #checks every card against eachother and adds repeats to a list
                    
        #print(repeats)

        rep=[] #new repeats
        
        for card in repeats:
            
            #print(rep)
            #print(card)
            
            if card not in rep:
                rep.append(card)

        repeats=rep #removes duplicates

        #print(repeats)

        if repeats != []:
            for i in range(int(len(repeats)/2)):
                cards.remove(repeats[i+1]) #remove duplicates
            
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
        
    def straight(hand,table):

        cards=hand+table
        straight=[]

        #print('in straight'+str(cards))
        
        cards=sorted(cards,reverse=True) #sort cards high to low

        #print(cards)

        repeats=[]

        for card1 in cards:
            for card2 in cards:
                if card1[0]==card2[0] and card1!=card2:
                    repeats.append(card2) #checks every card against eachother and adds repeats to a list
                    
        #print(repeats)

        rep=[] #new repeats
        
        for card in repeats:
            
            #print(rep)
            #print(card)
            
            if card not in rep:
                rep.append(card)

        repeats=rep #removes duplicates

        #print(repeats)

        if repeats != []:
            for i in range(int(len(repeats)/2)):
                cards.remove(repeats[i+1]) #remove duplicates
            
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

        a=check.wrapstraight(hand, table) #check if wrap

        if a!=False:

            for card in a[1]:
                if card[0]=='01':
                    card[0]='14' #convert ace back
            return a
        
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
            return check.similarend(2,similar,cards)

        
        if len(similar)==4: #if two pair
            return check.similarend(3,similar,cards)

        if len(similar)==6: #either 3 of a kind or 3 pairs
            if similar[0][0]==similar[2][0]:# 3 of a kind
                for i in range(3):
                    similar.remove(similar[1+i]) #remove duplicates

                return check.similarend(4,similar,cards)

            else: #3 pairs
                
                similar.remove(similar[-1])
                similar.remove(similar[-1]) #remove lowest pair

                return check.similarend(3,similar,cards)
            

        if len(similar)==8: #full house


            if similar[0][0]!=similar[2][0]: #if pair is before 3 of a kind

                similar=similar[2:9]+similar[0:2]

                #print(similar)
            
            for i in range(3):
                similar.remove(similar[1+i]) #remove duplicates

            return [7,similar]


        if len(similar)==12: #4 of a kind

            for i in range(4):
                similar.remove(similar[1+i])
                similar.remove(similar[1+i]) #remove duplicates
            
            return check.similarend(2,similar,cards)

        else: #if nothing is made
            cards=sorted(cards, reverse=True)
            while len(cards)>5:
                cards.remove(cards[-1])
            return [1,cards]

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
        
        if check.connect(cards)!=False and len(cards)==5: #if flush is also straight

            number=''
            for card in cards:
                number=number+card[0]
            
            return '09'+number

    result=max(results)

    number=''

    for card in result[1]:
        number=number+card[0]

    if result[0]==5: #if straight
        if number[2:4]=='05': #if wrap around
            number='0504030214'
    
    return str(result[0])+number

def convert(num):
    if num==9:
        return 'Straight-Flush'
    if num==8:
        return '4 of a Kind'
    if num==7:
        return 'Full House'
    if num==6:
        return 'Flush'
    if num==5:
        return 'Straight'
    if num==4:
        return '3 of a Kind'
    if num==3:
        return '2 Pairs'
    if num==2:
        return 'Pair'
    if num==1:
        return 'High Card'

def drawcheck(ranked):
    winner=ranked[0]

    draws=[winner]


    for i in range(len(ranked)-1):
        if ranked[i+1]==winner:
            draws.append(ranked[i+1])

    return draws

def newdata(players,hands,table):

    empty='0 0 0'

    for i in range(players-1):
        empty=empty+';'+str(i+1)+' 0 0'

    #print(empty)

    data=np.matrix(empty)

    for i in range(players):

        score=result(hands[i],table)
        score1=score[0:5]
        score2=score[5:11]
        
        data[i,1]=int(score1)
        data[i,2]=int(score2)

    for j in range(players+1): #order by score1
        for i in range(players-1):
            if data[i,1]<data[i+1,1]:
                data[[i,i+1]]=data[[i+1,i]]

    #print(str(data)+'\n\n')

    for j in range(players+1):
        pos=0
        #print('pos='+str(pos))
        var1=data[pos,1]
        var2=data[pos+1,1]
        #print(var1)
        #print(var2)
        while var1==var2 and pos<(players-1): #if score1 same order by score2
            #print('pos='+str(pos))
            var1=data[pos,2]
            var2=data[pos+1,2]
            #print(data[pos,2])
            #print(data[pos+1,2])
            if var1<var2:
                #print('less')
                
                data[[pos,pos+1]]=data[[pos+1,pos]]
            pos=pos+1
            
        
    return data

def play(players):

    newdeck() #generates new deck
    
    hands=deal(players) #deals players
    
    #print('Hands:')
    #for hand in hands:
        #print(hand) #displays hands

    table=playtable()
    #print('\nTable:\n'+str(table)+'\n') #deals table and shows

    data=newdata(players,hands,table)

    

    #print(data)

    winners=[]

    top=data[0,1:3]

    #print(top)

    pos=0
    while str(top)==str(data[pos,1:3]) and pos<(players-1):
        winners.append(data[pos,0])
        pos=pos+1

    #print(winners)

    typeofhand=convert(int(str(data[0,1])[0]))

    #print(typeofhand)

    winnerhands=[]

    for num in winners:
        winnerhands.append(hands[num])

    if len(winners)>1:

        

        return ['draw',winnerhands,typeofhand]

        
    else:

        return ['win',winnerhands,typeofhand]

def mixed():

    while True:
        for i in range(9):
            f=open(str(i+2)+'people.txt','a')
            f.write(str(play(i+2))+'\n')
            f.close()

def million():
    for i in range(1000000):
        if i%1000==0:
            print(i)
        f=open('2people.txt','a')
        f.write(str(play(2))+'\n')
        f.close()
        
def groupedmillion(players):
    for i in range(1000):
        towrite=''
        for j in range(1000):
            towrite=towrite+str(play(players))+'\n'
        f=open(str(players)+'people1.txt','a')
        f.write(towrite)
        f.close()
        print(str((i+1)/10)+'%')



groupedmillion(2)
groupedmillion(4)
groupedmillion(6)
groupedmillion(8)
groupedmillion(10)
groupedmillion(12)
groupedmillion(14)
groupedmillion(16)
groupedmillion(18)
groupedmillion(20)
groupedmillion(22)
