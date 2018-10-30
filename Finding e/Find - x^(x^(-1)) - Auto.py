import numpy as np
import math
import decimal
rep=int(input('Using the theory that the maximun of the function:\nf(x)=x^(x^(-1)) is e\nhow many rounds of accuray?'))
acc=.1
def f(x):
    return(x**(1/x))
low=2+acc
high=3
for i in range(rep):
    x=np.arange(low,high,acc)
    y=[]
    for i in range(len(x)):
        y.append(f(x[i]))
    out=x[y.index(max(y))]
    print(str(out)+' is '+str(math.exp(1)-float(out))+' off \n'+str(math.exp(1)))
    low=decimal.Decimal(out-acc)
    high=decimal.Decimal(out+acc)
    acc=decimal.Decimal(acc/10)
