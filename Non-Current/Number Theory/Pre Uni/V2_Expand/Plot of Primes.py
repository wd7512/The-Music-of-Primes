import matplotlib.pyplot as plt
f=open('PlistV2.txt','r')
maxx=len(f.readlines())
num=int(input('How many primes do we want to plot up to?\nthe max is '+str(maxx)+' type 0 for max\n:'))
f.close()
a=0
if num==0:
    num=maxx-1
f=open('PlistV2.txt','r')
data=[]
while a!=num:# recieves data in str form
    data.append(f.readline())
    a=a+1
f.close()
for i in range(len(data)):# converts the list items into integers
    data[i] = int(data[i])
plt.plot(data)
plt.ylabel('prime numbers')
plt.show()
