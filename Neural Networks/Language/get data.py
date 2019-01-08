import random
f=open('English-58000.txt','r')
g=open('English-14500-Read.txt','a')
data=f.readlines()
size=[]
for char in data:
    size.append(len(char))
print(max(size))
f.close()
f=open('English-58000.txt','r')
app=[]
for i in range(14500):
    line=f.readline()
    #print(line)
    app.append(line)
    f.readline()
    f.readline()
    f.readline()
ran=random.sample(app,14500)

for word in ran:
    g.write(str(word))
f.close()
g.close()
