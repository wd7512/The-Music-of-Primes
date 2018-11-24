import math
#import time
#tim=time.time()
f=open('Pseudo.txt','r')
a=f.readlines()
a=int(a[-1])
f.close()
print(a)
num=int(input('How many more numbers do you want to go up to?'))
def ftest(n):
    if (2**(n-1))%n==1:
        return True
    return False
def btest(n):
    for i in range(int(math.sqrt(n)//1)):
        if n%(i+2)==0:
            return False
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
