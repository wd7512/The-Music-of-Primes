import matplotlib.pyplot as plt

def sn(lastterms,coeff,c):
    res=0+c
    for i in range(len(coeff)):
        res=res+float(lastterms[i])*float(coeff[i])

    

    return res

order=int(input('Order: '))
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
equa='Uₙ='
coeffstr=[]
for i in range(order):
    a='X'+str(i+1)
    coeffstr.append(a)
    b='Uₙ-'+str(i+1)
    equa=equa+a+b+'+'
print(equa.translate(SUB)+'c')

coeff=[]

for name in coeffstr:
    coeff.append(float(input(name.translate(SUB)+ ': ')))
const=float(input('c: '))

terms=[]
for i in range(order):
    terms.append(float(input(('U'+str(i)).translate(SUB)+': ')))

num=int(input('How many terms: '))
for i in range(num):
    termz=[]
    for j in range(order):
        termz.append(terms[-(j+1)])
    res=sn(termz,coeff,const)
    terms.append(res)
    print(res)
#print(terms)
plt.plot(terms)
plt.show()
