f=open('English-58000.txt','r')
g=open('English-14500.txt','a')
data=f.readlines()
size=[]
for char in data:
    size.append(len(char))
print(max(size))
for i in range(14500):
    g.write(f.readline())
    f.readline()
    f.readline()
    f.readline()
f.close()
g.close()
