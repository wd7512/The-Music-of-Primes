import ast
import matplotlib.pyplot as plt
def vortex(n):
    a=0
    for i in range(len(str(n))):
        a=a+int(str(n)[i])
    if a>9:
        vortex(a)
    else:
        return(a)
f=open('Factors.txt', 'r')
y=ast.literal_eval(f.readline())
f.close()
n=int(input('How many numbers do you want to go up to?\n0 for max\nn:'))
if n==0:
    n=len(y)
x=[]
for i in range(len(y)):
    x.append(vortex(i))
plt.plot(x,y,'o')
plt.xlabel('Vortex')
plt.ylabel('Factors')
plt.show()
