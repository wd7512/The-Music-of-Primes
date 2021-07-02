import matplotlib.pyplot as plt
import numpy as np

def OneDefvsNAtt(n):
    out = 0
    for i in range(6):
        out = out + (i+1)**n

    return out/(6**(n+1))

def NDefvsOneAtt(n):
    out = 0
    for i in range(5):
        out = out + (i+1)**n

    return 1 - out/(6**(n+1))

def NDefvsNAtt(n):
    def aux(nums,n):
        if n == 0:
            return nums
        else:
            out = []
            for i in range(6):
                i = i + 1
                for num in nums:
                    out.append(i * num)

            return aux(out,n-1)

    if n < 1:
        return False
    else:
        nums = [i+1 for i in range(6)]
        return sum(aux(nums,n-1)) / 6**(2*n)

def brute(A,D,n): #we calculate chance that all def wins
    out = 0
    for i in range(n):
        defRolls = [np.random.randint(1,7) for i in range(D)]
        attRolls = [np.random.randint(1,7) for i in range(A)]

        defRolls = sorted(defRolls)
        attRolls = sorted(attRolls)

        win = True
        for i in range(min([A,D])):
            DiceD = defRolls[i]
            DiceA = attRolls[i]

            if DiceA > DiceD:
                win = False

        if win == True:
            out = out + 1

    return out / n
            
        
    
        


    
                

#plt.plot([OneDefvsNAtt(i) for i in range(21)])
#plt.plot([NDefvsOneAtt(i) for i in range(21)])
plt.plot([NDefvsNAtt(i) for i in range(10)])

plt.plot([brute(i,i,10000) for i in range(10)])
plt.show()
