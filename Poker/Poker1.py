#cards are coded with number and first letter of suit
#e.g. 8S,8D,8H,8C  in string form
#spades,diamonds,hearts,clubs
def checkplayers():#number of players
    number=4
    return number

def checkmoney():#current money
    money=500
    return money

def checkhand():#cards in hand
    card1=input('Card1 :')
    hand=['','']
    return hand

def checktable():#cards in hand
    table=['','','']
    return table

def checkcards():#current cards
    hand=checkhand()#2 cards in hand
    table=checktable()#cards on table
    cards=hand+table
    return hand+table

def fullprobability():
    if len(checkcards())>=5:
        return 1
    else:
        return 2
players=checkplayers()
money=checkmoney()
