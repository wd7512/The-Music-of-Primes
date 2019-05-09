import random
import matplotlib.pyplot as plt

money=100
start=5
percent=42

record=[money]
multiplier=0

def play(start,record,multiplier,percent,rounds):
    for i in range(rounds):
        bet=start*2**multiplier
        if bet>record[-1]:
            multiplier=0
            bet=start*2**multiplier
        
        newmoney=record[-1]
        if random.randint(0,1)<1:
            newmoney=newmoney+bet
            multiplier=0
        else:
            newmoney=newmoney-bet
            multiplier=multiplier+1
            if multiplier==4:
                multiplier=0
            
        record.append(newmoney)

        
        
    return record

record=play(start,record,0,50,1000000)
plt.plot(record)
plt.show()
