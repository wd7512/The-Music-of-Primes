import math
import ast
import matplotlib.pyplot as plt
global per
per=0
f=open('Factors.txt','r')
y=f.readline()
f.close()
f=open('PlistV2.txt','r')
primelist=f.readlines()
f.close()
y=ast.literal_eval(y)
yc=len(y)
n=int(input('How many to calculate?'))
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
    if math.floor((100*i)/n)%1==0 and math.floor((100*i)/n)!=0 and math.floor((100*i)/n)>math.floor((100*(i-1))/n):
        print(str(per)+'% Calculated')
        per=per+1
print('Completed\nWriting...Do not exit')
f=open('Factors.txt','w')
f.write(str(y))
f.close()
print('Completed')
nxt=input('Total='+str(len(y))+'\nPress enter to finish')
