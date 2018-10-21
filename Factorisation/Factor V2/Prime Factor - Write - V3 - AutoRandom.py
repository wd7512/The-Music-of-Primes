import math
import ast
import time
import random
import socket
runs=int(input('How many run throughs?\n:'))
runt=runs
while runs>0:
    print('run '+str(runt-runs+1))
    per=1
    f=open('Factors.txt','r')
    y=f.readline()
    f.close()
    f=open('PlistV2.txt','r')
    primelist=f.readlines()
    f.close()
    y=ast.literal_eval(y)
    yc=len(y)
    n=random.randint(1900, 2500)#Random Limits
    tim=[yc,socket.gethostname(),n]
    print('Calculating '+str(n)+' points...')
    for i in range(len(primelist)):#turns all strings in prime list to useable integers
        primelist[i]=int(primelist[i])
    dif=time.time()
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
    print('Completed\nWriting Time Data')
    tim.append(time.time()-dif)
    f=open('TimeData.txt', 'a')
    f.write('\n'+str(tim))
    f.close()
    runs=runs-1
nxt=input('Total='+str(len(y))+'\nPress enter to finish')
