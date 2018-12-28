import random
global deck

def newdeck():
    global deck
    deck=[]
    
    values=[0,1,2,3,4,5,6,7,8,9,10,11,12] #cards shifted down by 1
    suits=['D','S','C','H']
    
    for suit in suits:
        for value in values:
            deck.append([value,suit])
    
    deck=random.sample(deck,52) #shuffle deck

def draw(): 
    global deck

    card=deck[0]
    deck.remove(card)

    return card

def dealclock():
    global deck
    clock=[]
    for i in range(12):
        clockarm=[]
        for i in range(4):
            clockarm.append(draw())
        clock.append(clockarm)

    return clock

def play():

    newdeck()
    clock=dealclock()
    middle=deck #last 4 remaining cards
    strikes=3 #number of cards in middle
    
    card=middle[0] #top card
    middle.remove(card) #take it away

    while strikes>0:
        #print(strikes)
        #print(card)
        if card[0]==12: #if king
            strikes=strikes-1

            card=middle[0] #top card
            middle.remove(card) #take it away
        else:
            num=card[0]
            #print(num)
            card=clock[num][0]
            #print(card)
            #print(clock[num])
            clock[num].remove(card)

    count=0
    for sets in clock: #counts how many empty sets
        if sets==[]:
            count=count+1

    if count==12: #if all sets empty
        return True
    else:
        return False
def sim(howmanytimes):

    f=open('Clock Results.txt', 'r')
    line=f.readline()
    fail=int(line[6:])
    #print(fail)
    line=f.readline()
    suc=int(line[12:])
    #print(suc)
    f.close()
    for i in range(howmanytimes):
        sim=play()
        if sim==True:
            suc=suc+1
        if sim==False:
            fail=fail+1
    total=suc+fail
    f=open('Clock Results.txt','w')
    f.write('Fail: '+str(fail)+'\n')
    f.write('Successful: '+str(suc)+'\n')
    f.write('% Chance of Winning: '+str(round(100*suc/total,3))+'%')
    f.close()

    f=open('Clock Results - Overtime.txt','a')
    f.write(str([total,100*suc/total])+'\n') #runs and percent
    f.close()

    line1=''
    a=len(str(total))+4
    while a > 0:
        line1=(line1+"*")
        a=a-1
    print(line1)
    print("* "+str(total)+" *")
    print(line1)
    
    print('Fail: '+str(fail)+'\n')
    print('Successful: '+str(suc)+'\n')
    print('% Chance of Winning: '+str(round(100*suc/total,7))+'%')

while True:
    sim(100000)
    
