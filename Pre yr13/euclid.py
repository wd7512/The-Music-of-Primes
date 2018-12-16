import math
import sys
import Decimal
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")# makes numbers subscript
print('Using Euclids proof we will find another\nprime number greater than the specified\nnumber of primes we find up to')
upto=int(input('Euclids Proof of infinate prime numbers\nWith X=[P1*P2*P3....Pₙ]\nwhat do you want to set as\nn:'.translate(SUB)))
# this inputs the max prime number we go up to
if upto<2:
    fin=input('n must be greater than 1')
    quit()
sys.setrecursionlimit(upto**2)
speed=int(input('Large values of n can take long time to calculate\nwhich display would you like?\n1-Full(slow)\n2-Without Calculations(medium)\n3-Steps Only(fast)\n4-Result Only(fastest)\n:'))
if speed!=1 and speed!=2 and speed!=3 and speed!=4:# making programme more efficient
    fin=input('invalid input')
    quit()
a=b=2
primenums=[2]
def findprime(upto, a, b, primenums):# function to find n prime numbers and put them into a list
    if len(primenums)==upto: #are there the require amount of prime numbers?
        if speed !=4:
            nxt=input('completed finding primes\n'+str(primenums)+'\nPress enter to move onto next step')
        calc(primenums)
    else:
        a=b=a+1
        checkprime(upto, a, b, primenums)
def checkprime(upto, a, b, primenums):
    while b>1:#loop where factors of a is found RECURSION ERROR
        b=b-1
        if speed==1:
            print(str(a)+'%'+str(b)+'='+str(a%b))
        if b==1:# when divisor gets down to 1 the number is added to the list as it is prime
            primenums.append(a)
            if speed!=4:
                print(str(a)+' prime')
                if speed==1:
                    print(str(primenums))
            findprime(upto, a, b, primenums)
        elif a%b==0:# if factor is found, not prime
            if speed<3:
                print(str(a)+' not prime')
            findprime(upto, a, b, primenums)
def calc(primenums): #calculating X
    if speed!=4:
        print('Your list of prime numbers:\n'+str(primenums))
    c=1
    X=primenums[0]
    while c<len(primenums): #Summing the list into X
        X=X*primenums[c]
        if speed==1:
            print(str(X/primenums[c])+'*'+str(primenums[c])+'='+str(X))
        c=c+1
    X=X+1# final number
    if speed!=4:
        nxt=input('X='+str(X)+'\npress enter to move onto next step')
    check(X, primenums)
def check(X, primenums):
    e=primenums[-1]
    while e<Decimal(round(math.sqrt(X))+1):
        e=e+1
        if speed==1:
            print(str(X)+'%'+str(e)+'='+str(X%e))
        if X%e==0:
            if speed!=4:
                fin=input(str(X)+' is not prime but it is divisiable\nby '+str(e)+'\nPress enter to move onto next step')
            X=e
            check(X, primenums)
    fin=input(str(X)+' is prime')
    quit()
findprime(upto, a, b, primenums)
