import ast
numfiles=int(input('How many files?:'))
for i in range(numfiles):
    f=open('2people'+str(i+1)+'.txt','r')
    lines=f.readlines()
    for line in lines:
        line=ast.literal_eval(line)
