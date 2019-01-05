#2 layers
#connections, top row is input 1, bottom row input 2
import numpy as np
import random
def randomconnect():
    return np.matrix(str(random.randint(0,1))+' '+str(random.randint(0,1))+';'+str(random.randint(0,1))+' '+str(random.randint(0,1)))

var1=float(input('Input One, (0-1):'))
var2=float(input('Input Two, (0-1):'))
inputs=np.matrix(str(var1)+' '+str(var2))
outputs=inputs*connections
