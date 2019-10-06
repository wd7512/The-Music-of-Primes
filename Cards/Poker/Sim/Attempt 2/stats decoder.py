import ast
#ast.literal_eval()
def decode(file,hand,suited):
    cent = 1000000/100
    ccount = 0
    centcount = 0
    
    f = open(file,'r')

    handrev = [hand[1],hand[0]]

    data = f.readlines()
    f.close()
    useful = []
    wins = 0
    draws = 0
    for line in data:
        line = ast.literal_eval(line)
        cards1 = [line[0][0][0],line[0][1][0]]
        cards2 = [line[2][0][0],line[2][1][0]]

        if ccount % cent == 0:
            print(str(centcount)+'% complete')
            centcount = centcount + 1
        ccount = ccount + 1
        
        if suited == 0:
            if hand == cards1 or handrev == cards1:
                
                if line[4] == True:
                    draws = draws + 1
                else:
                    wins = wins + 1
                useful.append(line[1])
            if hand == cards2 or handrev == cards2:
                
                if line[4] == True:
                    draws = draws + 1
                useful.append(line[3])
                
        if suited == 1:
            if (hand == cards1 or handrev == cards1) and line[0][0][1] != line[0][1][1]:
                
                if line[4] == True:
                    draws = draws + 1
                else:
                    wins = wins + 1
                useful.append(line[1])
                
            if (hand == cards2 or handrev == cards2) and line[2][0][1] != line[2][1][1]:
                
                if line[4] == True:
                    wins = wins + 0.5
                useful.append(line[3])

        if suited == 2:
            if (hand == cards1 or handrev == cards1) and line[0][0][1] == line[0][1][1]:
                
                if line[4] == True:
                    draws = draws + 1
                else:
                    wins = wins + 1
                useful.append(line[1])
                
            if (hand == cards2 or handrev == cards2) and line[2][0][1] == line[2][1][1]:
                
                if line[4] == True:
                    draws = draws + 1
                useful.append(line[3])
                
    useful = sorted(useful)
    nameref = ['Straight Flush',
               'Quads',
               'Full House',
               'Flush',
               'Straight',
               'Three of a Kind',
               'Two Pair',
               'One Pair',
               'High Card']
    typefreq = []
    for name in nameref:
        typefreq.append(useful.count(name))

    compress = []

    tot = sum(typefreq)
    suitprint = suits(suited)
    print(str(tot)+' instances found of '+suitprint+' '+str(hand)+'\n')
    
    compress.append([tot,'instances'])

    winpercent = round(wins/tot * 100,2)
    drawpercent = round(draws/tot * 100,2)
    combpercent = round(winpercent + drawpercent, 2)

    print(str(winpercent)+'% win percentage')
    compress.append([winpercent,'win percentage'])
    print(str(drawpercent)+'% draw percentage')
    compress.append([drawpercent,'draw percentage'])
    print(str(combpercent)+'% combined win percentage\n')
    compress.append([combpercent,'combined win percentage'])

    typepercent = []
    for freq in typefreq:
        typepercent.append(round(freq/tot*100,4))
    for i in range(len(typepercent)):
        space = ''
        siz = 7 - len(str(typepercent[i]))
        for j in range(siz):
            space = space + ' '
        print(str(typepercent[i])+'%'+space+' --- '+str(nameref[i]))
        compress.append([typepercent[i],nameref[i]])

    return compress

def suits(num):
    if num == 0:
        suitprint = 'any'
    if num == 1:
        suitprint = 'offsuit'
    if num == 2:
        suitprint = 'suited'
    return suitprint

def save(data,filename):
    f = open(filename,'w')
    for b in data:
        f.write(str(b)+'\n')
    f.close()
    
def run(hand,suited,flop):
    
    if flop == True:
        file = 'Headsupflop-1000000 runs.txt'
        filename = str(hand)+str(suited)+' flop.txt'
    else:
        file = 'Headsup-1000000 runs.txt'
        filename = str(hand)+str(suited)+' river.txt'
    #hand = [int(input('Card Value 1:')),int(input('Card Value 2:'))] #[num1,num2]
    #suited = int(input('Suited? (0-both,1-off,2-on):'))

    save(decode(file,hand,suited),filename)

for i in range(13):
    for j in range(13-i-1):
        hand = [i+2,j+3+i]
        print(hand)
        run(hand,0,True)
        run(hand,1,True)
        run(hand,0,False)
        run(hand,1,False)
