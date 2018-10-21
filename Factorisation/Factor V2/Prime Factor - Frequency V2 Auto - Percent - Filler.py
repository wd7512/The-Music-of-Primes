import math
import matplotlib.pyplot as plt
import ast
global n
global y
global acc
f=open('Factors.txt', 'r')
y=ast.literal_eval(f.readline())
f.close()
n=int(input('How many numbers do you want to go up to?\n0 for max\nn:'))
if n==0:
    n=len(y)
acc=int(input('What percent range do you want\nThe larger the smoother but less accurate'))
axi=[]
for i in range(max(y)):
    axi.append(i)
def y1(r):
    a=0
    y1=[]
    for i in range(n):
        if y[i]==r:
            a=a+1
        if i%acc==0:
            y1.append(a/acc)
            a=0
    return(y1)
def y2(s):
    y2=y1(s)
    for i in range(s-1):
        y2=[a + b for a, b in zip(y2, y1(i+1))]
    return(y2)
x=[]
for i in range(len(y2(0))):
    x.append(acc*(i))
for i in range(len(axi)):
    plt.plot(x, y2(axi[i]), label=str(axi[i])+' Factors')
    plt.fill_between(x, y2(axi[i]-1), y2(axi[i]))
plt.xlabel('Number')
plt.ylabel('Percent')
plt.grid(True)
plt.legend()
plt.show()


