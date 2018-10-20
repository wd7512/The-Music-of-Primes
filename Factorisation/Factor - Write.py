import math
import ast
n=int(input('How many numbers do you want to add?\nn:'))
f=open('PlistV2.txt','r')
primelist=f.readlines()
f.close()
f=open('Factors.txt','r')
y=f.readline()
f.close()
y=ast.literal_eval(y)
print(y)
yc=len(y)
for i in range(len(primelist)):
    primelist[i]=int(primelist[i])
for i in range(n+1):
    a=0
    b=0
    c=i+yc
    while primelist[b]<=math.floor((c/2)):
        if c%primelist[b]==0:
            a=a+1
        b=b+1
    if a==0:
        y.append(1)
    else:
        y.append(a)
print(y)
f=open('Factors.txt','w')
f.write(str(y))
f.close()
