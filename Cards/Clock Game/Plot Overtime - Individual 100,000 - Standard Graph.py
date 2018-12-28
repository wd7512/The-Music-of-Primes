import matplotlib.pyplot as plt
import ast
#plots the % found in each 100,000 chunk
f=open('Clock Results - Overtime.txt','r')
data=f.readlines()
f.close()
x=[]
y=[]
z=[]
for point in data:
    point=ast.literal_eval(point)
    if point[0]%100000==0:
        #print(point)
        x.append(point[0])
        y.append(point[1])
for i in range(len(y)):
    if i==0:
        z.append(y[0])
    else:
        num=(i+1)*y[i]-i*y[i-1]
        z.append(num)
b=[] #bars
f=[] #frequency
ranger=max(z)-min(z)
numbar=40 #number of bars
split=ranger/numbar
for i in range(numbar):
    mina=min(z)+i*split
    maxa=min(z)+(i+1)*split
    b.append((mina+maxa)/1.75)

    count=0
    for num in z:
        if num>=mina:
            if num<maxa:
                count=count+1
    f.append(count)

plt.xlabel('bar size='+str(split))    
plt.bar(b,f,width=split)


plt.show()
