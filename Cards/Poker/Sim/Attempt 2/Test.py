import random
import os
import ast
import tkinter
allfiles = os.listdir()
filenames = []
for file in allfiles:
    if file[0] == '[':
        #print(file)
        filenames.append(file)



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
'''
score = 0
rounds = int(input('No. of Rounds:'))
for i in range(rounds):
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
    score = score + abs(test[0]-ans)

print(score/rounds)
'''
window = tkinter.Tk()
window.title('Poker Test')

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

tkinter.Checkbutton(window, text = 'High Card',variable = High,onvalue = True, offvalue=False).grid(row=0)
tkinter.Checkbutton(window, text = 'One Pair',variable = One,onvalue = True, offvalue=False).grid(row=1)
tkinter.Checkbutton(window, text = 'Two Pair',variable = Two,onvalue = True, offvalue=False).grid(row=2)
tkinter.Checkbutton(window, text = 'Three of a Kind',variable = Three,onvalue = True, offvalue=False).grid(row=3)
tkinter.Checkbutton(window, text = 'Straight',variable = Straight,onvalue = True, offvalue=False).grid(row=4)
tkinter.Checkbutton(window, text = 'Flush',variable = Flush,onvalue = True, offvalue=False).grid(row=5)
tkinter.Checkbutton(window, text = 'Full House',variable = Full,onvalue = True, offvalue=False).grid(row=6)
tkinter.Checkbutton(window, text = 'Quads',variable = Quads,onvalue = True, offvalue=False).grid(row=7)
tkinter.Checkbutton(window, text = 'Straight Flush',variable = Straight_Flush,onvalue = True, offvalue=False).grid(row=8)




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
    

