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

def scoring(hand,table):

    #print([hand,table])
    
    total = hand + table
    total = sorted(total, reverse=True)

    #false is nothing, else returns [type,5 card values]

    flush = checkflush(total) 
    #print(flush)

    straight = checkstraight(total)
    if straight == False:
        straight == checkstraight(straightconv(total))
    
    #print(straight)

    straightflush = False

    if flush != False and straight != False:
        
        straightflush = checkstraightflush(total)
        if straightflush != False:
            return straightflush

    totalnums = []
    for card in total:
        totalnums.append(card[0])

    

    quads = checkquads(totalnums)
    if quads != False:
        return quads #return

    fullhouse = checkfullhouse(totalnums)
    if fullhouse != False:
        return fullhouse #return

    if flush != False:
        return flush #return

    if straight != False:
        return straight #return

    trips = checktrips(totalnums)
    if trips != False:
        return trips #return

    twopair = checktwopair(totalnums)
    if twopair != False:
        return twopair #return
    
    onepair = checkonepair(totalnums)
    if onepair != False:
        return onepair #return

    return ['High Card',totalnums[:5]]

def checkstraightflush(total):
    counter = [['H',0],['D',0],['C',0],['S',0]]
    for card in total:
        for count in counter:
            if count[0] == card[1]:
                count[1] += 1

    for count in counter:
        if count[1] > 4:
            suit = count[0]

    suitedcards = []
    for card in total:
        if card[1] == suit:
            suitedcards.append(card)

    straightflush = checkstraight(suitedcards)
    if straightflush == False:
        straightflush == checkstraight(straightconv(suitedcards))

    if straightflush == False:
        return False

    else:
        #print(['Straight Flush',straightflush[1],total])
        return ['Straight Flush',straightflush[1]]
    

def checkonepair(totalnums):

    pairs = []

    for num1 in totalnums:
        count = 0
        for num2 in totalnums:
            if num1 == num2:
                count = count + 1
        if count == 2:
            if num1 not in pairs:
                pairs.append(num1)

    if len(pairs) == 0:
        return False

    pair = pairs[0]

    totalnums.remove(pair)
    totalnums.remove(pair)

    cards = [pair,pair,totalnums[0],totalnums[1],totalnums[2]]

    return ['One Pair',cards]


def checktwopair(totalnums):

    pairs = []

    for num1 in totalnums:
        count = 0
        for num2 in totalnums:
            if num1 == num2:
                count = count + 1
        if count == 2:
            if num1 not in pairs:
                pairs.append(num1)

    if len(pairs) < 2:
        return False

    while len(pairs) > 2:
        pairs.remove(min(pairs))

    pair1 = max(pairs)
    pair2 = min(pairs)

    totalnums.remove(pair1)
    totalnums.remove(pair1)
    totalnums.remove(pair2)
    totalnums.remove(pair2)

    highcard = max(totalnums)
    

    cards = [pair1,pair1,pair2,pair2,highcard]

    return ['Two Pair',cards]
        

def checktrips(totalnums):
    
    trips = []
    
    for num1 in totalnums:
        count = 0
        for num2 in totalnums:
            if num1 == num2:
                count = count + 1
        if count == 3:
            if num1 not in trips:
                trips.append(num1)

    if len(trips) == 0:
        return False

    trip = max(trips)

    while trip in totalnums:
        totalnums.remove(trip)

    cards = [trip,trip,trip,totalnums[0],totalnums[1]]

    return ['Three of a Kind',cards]

def checkfullhouse(totalnums):


    trip = []
    pair = []
    for num1 in totalnums:
        count = 0
        for num2 in totalnums:
            if num1 == num2:
                count = count + 1
        if count == 3:
            trip1 = [num1,num1,num1]
            if trip1 not in trip:
                trip.append(trip1)
        if count == 2:
            pair1 = [num1,num1]
            if pair1 not in pair:
                pair.append(pair1)

    if trip == [] or pair == []:
        return False


    besttrip = max(trip)
    tri = besttrip[0]

    a = 0
    while pair[a][0] == tri:
        a = a + 1
        if a >= len(pair):
            return False

    return ['Full House',[tri,tri,tri,pair[a][0],pair[a][0]]]
            
            

    
def checkquads(totalnums): #checked

    for num1 in totalnums:
        count = 0
        for num2 in totalnums:
            if num1 == num2:
                count = count + 1
        if count == 4:
            a = 0
            last = totalnums[a]
            while totalnums[a] == num1:
                a = a + 1
                last = totalnums[a]
            return ['Quads',[num1,num1,num1,num1,last]]

    return False
        
    

def checkstraight(total):
    nums = [] #purely numbers
    for card in total:
        if card[0] not in nums:
            nums.append(card[0])


    if len(nums) < 5:
        return False

    if len(nums)==5 and (max(nums) - min(nums)) == 4:
        return (['Straight',nums])

    if len(nums) == 6:
        
        nums1 = nums[1:]
        nums2 = nums[:-1]

        if (max(nums1) - min(nums1)) == 4:
            return (['Straight',nums1])

        if (max(nums2) - min(nums2)) == 4:
            return (['Straight',nums2])

    if len(nums) == 7:

        nums1 = nums[2:]
        nums2 = nums[1:-1]
        nums3 = nums[:-2]

        if (max(nums1) - min(nums1)) == 4:
            return (['Straight',nums1])

        if (max(nums2) - min(nums2)) == 4:
            return (['Straight',nums2])

        if (max(nums3) - min(nums3)) == 4:
            return (['Straight',nums3])



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

            suitedcards=sorted(suitedcards, reverse=True)

            while len(suitedcards) > 5:
                suitedcards = suitedcards[:-1]

            output = []
            for card in suitedcards:
                output.append(card[0])

            return (['Flush',output])


    return False

def strengthconv(name,reverse):
    if name == 0:
        return 'Total'
    if reverse == False:
        if name == 'Straight Flush':
            return 10
        if name == 'Quads':
            return 9
        if name == 'Full House':
            return 8
        if name == 'Flush':
            return 7
        if name == 'Straight':
            return 6
        if name == 'Three of a Kind':
            return 5
        if name == 'Two Pair':
            return 4
        if name == 'One Pair':
            return 3
        if name == 'High Card':
            return 2
        
    if reverse == True:
        if name == 10:
            return 'Straight Flush'
        if name == 9:
            return 'Quads'
        if name == 8:
            return 'Full House'
        if name == 7:
            return 'Flush'
        if name == 6:
            return 'Straight'
        if name == 5:
            return 'Three of a Kind'
        if name == 4:
            return 'Two Pair'
        if name == 3:
            return 'One Pair'
        if name == 2:
            return 'High Card'
        


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

    if players == 1:
        return scoring(hands[0],table)

    scores = []

    for hand in hands:
        sc = scoring(hand,table)
        scores.append([strengthconv(sc[0],False),sc[1],hand])

    scores = sorted(scores,reverse=True)

    if players > 1:

        count = 1
        

    for score in scores:
        score[0] = strengthconv(score[0],True)
    

    return scores

def printcheck(real,ref,num):
    percent = round(100*real/ref-100,ndigits=3)
    print(strengthconv(num,True)+' : '+str(real)+' // '+str(ref)+' : '+str(percent)+'%')
    
def freqcheck():
    
    stfl=0
    quads=0
    fuho=0
    fl=0
    st=0
    trips=0
    tp=0
    op=0
    hc=0

    freq=[] #in order above
    totalfreq = 1000000
    for i in range(totalfreq):
        a=game(1)
        if a[0] == 'Flush':
            fl = fl + 1
        if a[0] == 'Straight':
            st = st + 1
        if a[0] == 'Quads':
            quads = quads + 1
        if a[0] == 'Straight Flush':
            stfl = stfl + 1
        if a[0] == 'Full House':
            fuho = fuho + 1
        if a[0] == 'Three of a Kind':
            trips = trips + 1
        if a[0] == 'Two Pair':
            tp = tp + 1
        if a[0] == 'One Pair':
            op = op + 1
        if a[0] == 'High Card':
            hc = hc + 1

    freq = [stfl,quads,fuho,fl,st,trips,tp,op,hc]
    refdec = [41584,224848,3473184,4047644,6180020,6461620,31433400,58627800,23294460]
    for i in range(len(refdec)):
        
        refdec[i] = refdec[i]/133784560 #total number -- 52C7

    ref = []
    for dec in refdec:
        ref.append(round(totalfreq*dec))


    print('Type : Observed // Expected : percent differance')
    for i in range(9):
        printcheck(freq[i],ref[i],10-i)
    printcheck(sum(freq),sum(ref),0)
    


