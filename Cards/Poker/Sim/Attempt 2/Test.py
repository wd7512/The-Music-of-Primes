import random
import os
import ast
allfiles = os.listdir()
filenames = []
for file in allfiles:
    if file[0] == '[':
        #print(file)
        filenames.append(file)

possibles = []

High = True
One = True
Two = True
Three = True
Straight = True
Flush = True
Full = True
Quads = True
Straight_Flush = True

if High == True:
    possibles.append('High Card')
if One == True:
    possibles.append('One Pair')
if Two == True:
    possibles.append('Two Pair')
if Three == True:
    possibles.append('Three of a Kind')
if Straight == True:
    possibles.append('Straight')
if Flush == True:
    possibles.append('Flush')
if Full == True:
    possibles.append('Full House')
if Quads == True:
    possibles.append('Quads')
if Straight_Flush == True:
    possibles.append('Straight Flush')

testfiles = []
flop = True
river = True

if flop == True:
    for file in filenames:
        if file[-5:] == 'p.txt':
            testfiles.append(file)
if river == True:
    for file in filenames:
        if file[-5:] == 'r.txt':
            testfiles.append(file)
    

def conv(filename):
    brek = filename.index(']')
    if filename[brek+1] == 0:
        sui = 'suited'
    else:
        sui = 'off-suit'

    name = filename[1:brek]
    if file[-5:] == 'r.txt':
        end = 'river'
    else:
        end = 'flop'

    return name +' '+ sui +' '+end


while True:
    file = random.choice(testfiles)
    f = open(file,'r')
    rawdata = f.readlines()
    f.close()
    data = []
    for a in rawdata:
        data.append(ast.literal_eval(a))
    cata = random.choice(possibles)
    for a in data:
        if a[1] == cata:
            test = a
    print(conv(file))
    ans = float(input(cata+' : '))
    print(str(test)+'\n')
