import sys
import math
f=open('PlistV1.txt','r')
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
typ=input('Do you want visual text?y/n')
def abc(count, more, divc, div, new, linelist, lastlist):
    new=new+1
    divc=0
    div=int(linelist[divc])
    while count!=more:
            while new%div!=0:
                if div>math.sqrt(int(linelist[-1])):
                    count=count+1
                    linelist.append(str(new)+'\n')
                    lastlist.append(str(new)+'\n')
                    print(lastlist)
                    abc(count, more, divc, div, new, linelist, lastlist)
                print(str(new)+'%'+str(div)+'='+str(new%div))
                divc=divc+1
                div=int(linelist[divc])
            abc(count, more, divc, div, new, linelist, lastlist)
            print(str(new)+'not prime')
    end=input('completed, enter to upload')
    upload(count, more, divc, div, new, linelist, lastlist)
def abcd(count, more, divc, div, new, linelist, lastlist):
    new=new+1
    divc=0
    div=int(linelist[divc])
    while count!=more:
            while new%div!=0:
                if div==int(linelist[-1]):
                    count=count+1
                    linelist.append(str(new)+'\n')
                    lastlist.append(str(new)+'\n')
                    abcd(count, more, divc, div, new, linelist, lastlist)
                divc=divc+1
                div=int(linelist[divc])
            abcd(count, more, divc, div, new, linelist, lastlist)
    end=input('completed, enter to upload')
    upload(count, more, divc, div, new, linelist, lastlist)
def upload(count, more, divc, div, new, linelist, lastlist):
    print('the largest prime is\n\n'+lastlist[-1])
    f=open('PlistV1.txt','a')
    for i in lastlist:
        f.write(i)
    f.close()
    end=input('completed')
    quit()
if typ=='y':
    abc(count, more, divc, div, new, linelist, lastlist)
if typ=='n':
    abcd(count, more, divc, div, new, linelist, lastlist)
