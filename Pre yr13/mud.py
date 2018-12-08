import time
with open('mud.txt','r') as f:
    a=f.readlines()
    f.close()
print('The last entry was\n'+a[len(a)-1])
num=int(input('0-10'))
with open('mud.txt','a+') as f:
    f.write('\n'+str(num)+'--'+(time.strftime("%H:%M:%S"))+'--'+(time.strftime("%d/%m/%Y")))
    f.close()

