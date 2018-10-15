import math
import time
n=int(input('Gauss Estimate of how many primes there are up to\nn:'))
a=2#First Prime
b=0#Counter
ty=input('Do you want to see the addition?\ny/n')
if ty!='y' and ty!='n':
        print('invalid input')
while a!=n:
        b=b+1/math.log(a)#Log Function
        a=a+1
        if ty=='y':
                print(b)
print(str(b)+'which means there is a '+str(n/b)+'%\nof a prime number up to '+str(n))
time.sleep(20)
