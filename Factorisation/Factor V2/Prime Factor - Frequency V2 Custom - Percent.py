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
print('Please list the \'number of factors\' lines\nyou would like to draw\ntype 0 when done')
axi=[]
ax=int(input(':'))
while ax!=0:
    axi.append(ax)
    ax=int(input(':'))
print(axi)
def y2(r):
    a=0
    y2=[]
    for i in range(n):
        if y[i]==r:
            a=a+1
        if i%acc==0:
            y2.append(a/acc)
            a=0
    return(y2)
for i in range(len(axi)):
    plt.plot(y2(axi[i]), label=str(axi[i])+' Factors')
plt.xlabel('Number')
plt.ylabel('Percent')
plt.legend()
plt.show()


