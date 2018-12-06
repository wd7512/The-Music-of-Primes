#cards are coded with number and first letter of suit
#e.g. 8S,8D,8H,8C  in string form
#spades,diamonds,hearts,clubs
def checkplayers():#number of players
    number=int(input('Number of Players :'))
    return number

def checkmoney():#current money
    money=int(input('Money :'))
    return money

def checkhand():#cards in hand
    card1=str(input('Card1 :'))
    card2=str(input('Card2 :'))
    hand=[card1,card2]
    return hand

def checktable(tablenum):#cards on table, tablenum=number of cards on table
    if tablenum==0:
        return
    table=[]
    for i in range(tablenum):
        table.append(str(input('Table'+str(i+1)+' :')))
    return table

def checkcards(tablenum):#current cards
    hand=checkhand()#2 cards in hand
    table=checktable(tablenum)#cards on table
    cards=hand+table
    return hand+table

def fullprobability(cards, players):
    if len(cards)==2:#pre-flop
        if (cards[0])[1]==(cards[1])[1]:
            cards=str((cards[0])[0])+str((cards[1])[0])+'s'
        else:
            cards=str((cards[0])[0])+str((cards[1])[0])
        print(cards)
        f=open(str(players)+'Players.txt','r')
        key=(f.readline())
        x=True
        while x==True:
            line=(f.readline()).split('\t')
            print(line)
            if len(cards)==3:#if suited
                cardswap=(cards[1]+cards[0]+cards[2])
            else:
                cardswap=(cards[1]+cards[0])
            if cards==(line)[1] or cardswap==line[1]:
                #print('found Card')
                x=False
        print(key)
        print(line)

    return
players=checkplayers()
money=checkmoney()
print('Pre-Flop')
hand=checkhand()
print(fullprobability(hand, players))
