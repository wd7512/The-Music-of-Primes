import math
import time
n=int(input('Gauss Estimate of how many primes there are up to\nn:'))
a=2
b=0
ty=input('Do you want to see the addition?\ny/n')
if ty!='y' and ty!='n':
        print('invalid input')
elif ty=='y':
    while a!=n:
        b=b+1/math.log(a)
        a=a+1
        print(b)
elif ty=='n':
    while a!=n:
        b=b+1/math.log(a)
        a=a+1
print(str(b)+'which means there is a '+str(n/b)+'%\nof a prime number up to '+str(n))
time.sleep(20)
