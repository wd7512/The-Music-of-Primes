#2 layers
#connections, top row is input 1, bottom row input 2
import numpy as np
from random import *
def randomconnect():
    return np.matrix(str(random.randint(0,1))+' '+str(random.randint(0,1))+';'+str(random.randint(0,1))+' '+str(random.randint(0,1)))

#var1=float(input('Input One, (0-1):'))
#var2=float(input('Input Two, (0-1):'))
#inputs=np.matrix(str(var1)+' '+str(var2))
#outputs=inputs*connections

def mastermind(length):
    if int(length)>0:
        length=(10**(int(length))-1)
        num=randint(1, (int(length)))
        trys=0
        guess='0'
        while int(num) != int(guess):
            num=list(str(num))
            guess=input((str(trys)+">"))
            trys=trys+1
            guess=list(guess)
            guess=str(''.join(guess))
            num=str(''.join(num))
            if len(guess) != len(num):
                end=input("Wrong number of integers inputted, \npress enter to end")
                quit()
            else:
                result=''
                pos=0
                for i in guess:
                    if i == num[pos:(pos+1)]:
                        result=(result+'*')
                    pos=pos+1
            print(result)
        return trys #number of guesses
    else:
        end=input("Invalid input, press enter to end")
        quit()

def round1():
    for i in range(100):
        mastermind(2)
