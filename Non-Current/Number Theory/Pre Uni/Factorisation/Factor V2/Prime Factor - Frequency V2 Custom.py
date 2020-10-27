import math
import matplotlib.pyplot as plt
import ast
global n
global y
f=open('Factors.txt', 'r')
y=ast.literal_eval(f.readline())
f.close()
n=int(input('How many numbers do you want to go up to?\n0 for max\nn:'))
if n==0:
    n=len(y)
print('Please list the \'number of factors\' lines\nyou would like to draw\ntype 0 when done')
axi=[]
ax=int(input(':'))
while ax!=0:
    axi.append(ax)
    ax=int(input(':'))
print(axi)
def y1(r):
    y1=[0]
    for i in range(n):#numbers of r less than n
        if y[i]==r:
            y1.append(y1[i]+1)
        else:
            y1.append(y1[i])
    return(y1)
for i in range(len(axi)):
    plt.plot(y1(axi[i]), label=str(axi[i])+' Factors')
plt.legend()
plt.show()
