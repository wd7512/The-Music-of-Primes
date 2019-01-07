#26*23 max word = 598 input vector
import numpy as np
alphabet=['A','B','C','D','E',
          'F','G','H','I','J',
          'K','L','M','N','O',
          'P','Q','R','S','T',
          'U','V','W','X','Y',
          'Z']
def start():
    f=open('Reading.txt','r')
    linesread=f.readline()
    print(linesread)
    linesread=int(linesread[12:])
    print(linesread)
    
    f.close()

    return linesread
def save(brain,linesread):
    linesread=start()
    f=open('Reading.txt','w')
    f.write('LINES READ: '+str(linesread)+'\n')
    f.write('\n'+str(brain[0])+'\n\n'+str(brain[1]))
    f.close()
    
def emptymatrix(x,y):
    a=''
    for i in range(x):
        a=a+'0 '
    b=''
    for i in range(y-1):
        b=b+a+';'
    b=b+a

    return np.matrix(b)
