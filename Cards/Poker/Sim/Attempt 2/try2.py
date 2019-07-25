import random

def newdeck(): #checked
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    suits = ['H','D','C','S']
    deck = []
    for value in values:
        for suit in suits:
            card = [value,suit]
            deck.append(card)
    random.shuffle(deck)
    return (deck)

def drawcard(deck): #checked
    card = deck[0]
    deck.remove(card)
    return [card,deck]

def score(hand,table):
    total = hand + table
    total = sorted(total)

    flush = checkflush(total) #false is nothing, else returns the flush cards
    straight = checkstraight(total)
    if straight == False:
        straight == checkstraight(straightconv(total))
    print(straight)

    return straight

def checkstraight(total):
    nums = [] #purely numbers
    for card in total:
        if card[0] not in nums:
            nums.append(card[0])


    if len(nums) < 5:
        return False

    if len(nums)==5 and (max(nums) - min(nums)) == 4:
        return(nums)

    if len(nums) == 6:
        if (max(nums) - min(nums)) == 4:
            return(nums)
        if (max(nums) - min(nums)) == 5:
            nums = nums[1:]
            return(nums)

    if len(nums) == 7:
        if (max(nums) - min(nums)) == 4:
            return(nums)
        if (max(nums) - min(nums)) == 5:
            nums = nums[1:]
            return(nums)
        if (max(nums) - min(nums)) == 6:
            nums = nums[2:]
            return(nums)



    return False

def straightconv(total): #checked
    totala = total[:]
    aces = []
    ones = []
    for card in totala:
        if card[0] == 14:
            aces.append(card)

    for card in aces:
        totala.remove(card)
        ones.append([1,card[1]])

    return ones + totala

def checkflush(total): #checked
    counter = [['H',0],['D',0],['C',0],['S',0]]
    for card in total:
        for count in counter:
            if count[0] == card[1]:
                count[1] += 1

    for count in counter:
        while count[1] > 4:
            suit = count[0]
            suitedcards = []
            for card in total:
                if card[1] == suit:
                    suitedcards.append(card)

            suitedcards=sorted(suitedcards)

            while len(suitedcards) > 5:
                suitedcards = suitedcards[1:]

            return suitedcards


    return False

def game(players):
    deck = newdeck()
    hands = []
    for x in range(players):
        card1, deck = drawcard(deck)
        card2, deck = drawcard(deck)
        hands.append([card1,card2])

    table = []
    for x in range(5):
        card, deck = drawcard(deck)
        table.append(card)

    return score(hands[0],table)

deck = newdeck()
total = []
for i in range(7):
    card , deck = drawcard(deck)
    total.append(card)


a=False
while a == False:
	a=game(1)
	print(a)
