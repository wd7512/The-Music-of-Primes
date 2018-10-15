import sys
import math
import time
f=open('PlistV2.txt','r')
linelist=f.readlines()
f.close()
print(linelist[-1])#prints last line of txt file
new=int(linelist[-1])#first number to test
count=0#a counter for the var more
divc=0
div=int(linelist[divc])# the prime divisor
more=int(input('How many more primes do we want to find?(max-825)\n'))
sys.setrecursionlimit(more**2+2000)
lastlist=[]
typ=input('Do you want visual calculations?y/n')
tim=input('Do you want to cap the CPU useage?y/n')
def abc(count, more, divc, div, new, linelist, lastlist, tim):
    new=new+1
    divc=0
    div=int(linelist[divc])
    while count!=more:
            while new%div!=0:
                if div>math.sqrt(int(linelist[-1])):
                    count=count+1
                    print(new)
                    f=open('PlistV2.txt','a')
                    f.write(str(new)+'\n')
                    f.close()
                    linelist.append(str(new)+'\n')
                    lastlist.append(str(new)+'\n')
                    print(lastlist)
                    abc(count, more, divc, div, new, linelist, lastlist, tim)
                if tim=='y':
                    time.sleep(0.01)
                print(str(new)+'%'+str(div)+'='+str(new%div))
                divc=divc+1
                div=int(linelist[divc])
            abc(count, more, divc, div, new, linelist, lastlist, tim)
            print(str(new)+'not prime')
    end=input('completed upload')
    quit()
def abcd(count, more, divc, div, new, linelist, lastlist, tim):
    new=new+1
    divc=0
    div=int(linelist[divc])
    while count!=more:
            while new%div!=0:
                if div>math.sqrt(int(linelist[-1])):
                    count=count+1
                    print(new)
                    f=open('PlistV2.txt','a')
                    f.write(str(new)+'\n')
                    f.close()
                    linelist.append(str(new)+'\n')
                    lastlist.append(str(new)+'\n')
                    abcd(count, more, divc, div, new, linelist, lastlist, tim)
                if tim=='y':
                    time.sleep(0.01)
                divc=divc+1
                div=int(linelist[divc])
            abcd(count, more, divc, div, new, linelist, lastlist, tim)
    end=input('completed upload')
    quit()
if tim=='y' or tim=='n':
    if typ=='y':
        abc(count, more, divc, div, new, linelist, lastlist, tim)
    if typ=='n':
        abcd(count, more, divc, div, new, linelist, lastlist, tim)

