import math
n=int(input('Number\n:'))
f=open('PlistV3.txt','r')
primelist=[]
i=int(f.readline())
primelist.append(i)
while i<int(math.sqrt(n)//1):
    i=int(f.readline())
    primelist.append(i)
f.close()
ob=len(primelist)
for i in range(len(primelist)):
    if n%(primelist[ob-i-1])==0:
        print('it is divisiable by '+str(primelist[ob-i-1])+'\nand therefore '+str(n/primelist[ob-i-1]))
        
