import ast
file='Classic 72 - Test.txt'
f=open(file,'r')
data=f.readlines()
f.close()
for a in data:
    if a=='\n':
        data.remove(a)
for i in range(len(data)):
    data[i]=ast.literal_eval(data[i])
coords=[] #coordinates
proximity=[] #distance between subsequent people
