import random
global deck



def newdeck(no):
    global deck
    deck=[]
    
    values=[2,3,4,5,6,7,8,9,10,11,12,13,14] 
    suits=['D','S','C','H']

    for i in range(no):
        for suit in suits:
            for value in values:
                deck.append([value,suit])
    
    deck=random.sample(deck,no*52) #shuffle deck

def draw(): 
    global deck

    card=deck[0]
    deck.remove(card)

    return card

def check(cards):
    counts=[0]
    for card in cards:
        #print(card)
        if card[0]==14: #if ace
            for i in range(len(counts)):
                counts[i]=counts[i]+1
                
            counts.append(counts[-1]+11)

        elif card[0] in [11,12,13]:
            for i in range(len(counts)):
                counts[i]=counts[i]+10
            
        else:
            for i in range(len(counts)):
                counts[i]=counts[i]+card[0]

    #print(counts)

    end=[]

    for count in counts:
        if count<22:
            end.append(count)
    #print(counts)

    if len(end)==0:
        return 'bust'
    else:
        return max(end)

def play(no,money): #no-number of decks
    
    newdeck(no)

    table=[]
    player=[]

    bet=int(input('('+str(money)+')Bet:'))

    while bet!=0:

        
        
        player.append(draw())
        table.append(draw())

        player.append(draw())
        table.append(draw())

        print('Table: '+str(table[0]))
        print('Your Cards('+str(check(player))+'):\n'+str(player))

        action=str(input('Stand-s or Hit-h:'))

        vara=True

        while vara==True:
            print(vara)
            
            if action=='h': #if hits
                
                player.append(draw())

                
                
            else:    
                print('Invalid Input\nPress s or h:')

            print('Your Cards('+str(check(player))+'):\n'+str(player))
            
            action=str(input('Stand-s or Hit-h:'))

            if action=='s':
                print('gdhsu')
                vara=False
            
            if check(player)=='bust':
                vara=False        
    

no=int(input('Number of Decks:'))
money=int(input('Starting money:'))
print('Bet 0 to end game')
play(no,money)
