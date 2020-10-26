#to use this create the file 'Add spaces.txt' and deposit text wanting to be converted
f=open('Add spaces.txt','r')
a=f.readlines()
f.close()
f=open('Add spaces.txt','w')
f.write('')
f.close()
f=open('Add spaces.txt','a')
for i in range(len(a)):
    a[i]=a[i].replace('\n','\n\n')
    print(a[i])
    f.write(a[i])
f.close()
