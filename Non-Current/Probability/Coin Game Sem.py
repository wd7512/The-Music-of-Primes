import random
import matplotlib.pyplot as plt

def func():
    trials = 10000
    players = 10000
    res = []
    for p in range(players):
        c = True
        count = 0
        for i in range(trials):
            if c == True:
                if random.randint(0,1) == 1:
                    count = count + 1
                else:
                    count = count - 1
                    
                if count == 0:
                    c = False
                    k = i + 0
                else:
                    k = players
        res.append(k)

    return sum(res)/len(res)

        
#xnum = [10**2,10**3,10**4,10**5,10**6]
xnum = range(10)
ynum = [func() for x in xnum]
plt.plot(xnum,ynum)
plt.show()
