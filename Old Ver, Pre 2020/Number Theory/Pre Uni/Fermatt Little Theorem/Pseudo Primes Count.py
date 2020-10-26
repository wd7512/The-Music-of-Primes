import math
#import time
#tim=time.time()
num=int(input('How many more numbers do you want to go up to?'))
f=open('Pseudo.txt','r')
a=f.readlines()
a=int(a[-1])
f.close()
print(a)
f=open('PlistV3.txt','r')
primelist=[]
primelist.append(f.readline())
while int(f.readline())<int(math.sqrt(a+num)//1):
    primelist.append(f.readline())
f.close()
print(primelist)
def ftest(n):
    if (2**(n-1))%n==1:
        return True
    return False
def btest(n):
    i=0
    while int(primelist[i])<int(math.sqrt(n)//1):
        if n%(int(primelist[i]))==0:
            return False
        i=i+1
    return True

pseudo=[]
for i in range(num):
    if ftest(i+1+a)==True:
        print(i+1+a)
        if btest(i+1+a)!=True:
            print(str(i+1+a)+'Error')
            pseudo.append(i+1+a)
#print(pseudo)
#print(tim-time.time())
#stop=input('oo')
f=open('Pseudo.txt', 'a')
for i in pseudo:
    f.write('\n'+str(i))
f.close()
