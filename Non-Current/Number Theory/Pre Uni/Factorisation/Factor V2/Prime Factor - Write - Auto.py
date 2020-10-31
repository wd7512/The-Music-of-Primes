import math
import ast
import matplotlib.pyplot as plt
f=open('Factors.txt','r')
y=f.readline()
f.close()
f=open('PlistV2.txt','r')
primelist=f.readlines()
f.close()
y=ast.literal_eval(y)
yc=len(y)
n=5000-math.floor(yc/50)
print('Calculating...')
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
print('Completed\nWriting...Do not exit')
f=open('Factors.txt','w')
f.write(str(y))
f.close()
print('Completed')
nxt=input('Total='+str(len(y))+'\nPress enter to finish')