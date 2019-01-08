import random
def english():
    f=open('English-14500.txt','r')
    g=open('English-3625.txt','a')
    data=f.readlines()
    size=[]
    for char in data:
        size.append(len(char))
    print(max(size))
    f.close()
    f=open('English-14500.txt','r')
    app=[]
    for i in range(3625):
        line=f.readline()
        #print(line)
        app.append(line)
        f.readline()
        f.readline()
        f.readline()
    ran=random.sample(app,3625)

    for word in ran:
        g.write(str(word))
    f.close()
    g.close()
def malay():
    f=open('Malay-50000.txt','r')
    data=f.readlines()
    f.close()
    newdata=[]
    for line in data:
        #print(line)
        a=line.split()
        
        
        newdata.append(a[0])
    print(newdata)
    newdata2=[]
    for word in newdata:
        newdata2.append(word.upper())
    with open('Malay-50000.txt', 'w', encoding='utf-8') as f:

        for word in newdata2:
        
            f.write(str(word)+'\n')
