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
    if suited == 0:
        suitprint = 'any'
    if suited == 1:
        suitprint = 'offsuit'
    if suited == 2:
        suitprint = 'suited'
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

file = 'Headsup-1000000 runs.txt'
#hand = [int(input('Card Value 1:')),int(input('Card Value 2:'))] #[num1,num2]
#suited = int(input('Suited? (0-both,1-off,2-on):'))

a=decode(file,[6,7],0)
