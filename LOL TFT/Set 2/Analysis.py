
def csv_conv(filename):
    f = open(filename,'r')
    data = f.readlines()
    f.close()
    output = []
    for line in data:
        
        newline = line.split(',')
        for i in range(len(newline)):
            if newline[i][-1:] == '\n':
                newline[i] = newline[i][:-1]
                
        output.append(newline)
    if len(output) == 1:
        return output[0]
    else:
        return output

def update_stats():
    champs = csv_conv('Champs.csv')
    
def clean(num):
    return round(num,10)

def save_csv(data,name):
    f = open(name+'.csv','w')
    strdata = [str(a) for a in data]
    f.write(','.join(strdata))
    f.close()

def level_three():
    champs = csv_conv('Champs.csv')[1:]
    for i in range(len(champs)):
        for j in range(len(champs[i])):
            try:
                champs[i][j] = int(champs[i][j])
            except ValueError:
                pass
                #print('not an int')
    level_prob = csv_conv('Level Chance.csv')
    
    three = level_prob[3]
    chance = [] #probabilities
    for a in [float(x) for x in three]:
        if a<1:
            chance.append(a)
    #print(chance)
            
    low_champs = [x for x in champs if int(x[1])<4] #champs below 4 cost
    for a in low_champs:
        print(a)

    freq = [0,0,0]

    for champ in low_champs:
        freq[champ[1]-1] = freq[champ[1]-1] + 1

    print(freq)
    expected = []
    for i in range(3):
        expected.append(clean(freq[i]*chance[i]))
    print(expected)
    
    
    

#a = csv_conv('Traits.csv')
#b = csv_conv('Champs.csv')

#.write(str(','.join(example)))
level_three()
