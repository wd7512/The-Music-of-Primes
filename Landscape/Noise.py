import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D
import math

def twnoise(size):
    res = [0,random.randint(-2,2)]
    

    for i in range(size-2):
        old = res[i+1]-res[i]
        if old > 0:
            res.append(res[i+1] + random.randint(0,old))
        elif old < 0:
            res.append(res[i+1] + random.randint(old,0))
        else:
            res.append(res[i+1] + random.randint(-1,1))
                    
    #plt.plot(res)
    #plt.show()

    return res

def thnoise(size):
    res = [twnoise(size)]
    s = size - 1

    for i in range(s):
        line = []
        for j in range(s):
            rate = res[i][j+1] - res[i][j]
            if rate > 0:
                line.append(res[i][j] + random.randint(0,rate))
            if rate < 0:
                line.append(res[i][j] + random.randint(rate,0))
            if rate == 0:
                line.append(res[i][j] + random.randint(-1,1))

                
        line.append(res[i][-1] + random.randint(-1,1))
        res.append(line)

    return [res,size]

def _thnoise(big,small):

    tot = (big-1) * (small) + 1
    res = []

    main,null = thnoise(big)
    
    ci = 0
    for i in range(tot):
        line = []
        cj = 0
        for j in range(tot):
            if i%big == 0 and j%big == 0:
                line.append(main[ci][cj])
                cj = cj + 1
            else:
                line.append(0)
        res.append(line)
        if cj > 0:
            ci = ci + 1

    
    plt.imshow(main)
    plt.show()
    plt.imshow(res)
    plt.show()
    
    

def thnoise_(size):
    lim = 150
    x = twnoise(size)
    for i in range(len(x)):
        x[i] = x[i]*5


    y = twnoise(size)
    for i in range(len(y)):
        y[i] = y[i]*5

        
    array = [x]
    for i in range(size-1):
        eline = [y[i+1]]
        for j in range(size-1):
            eline.append(0)
        array.append(eline)

    for i in range(size-1):
        for j in range(size-1):
            x_grad = array[i][j+1] - array[i][j]
            y_grad = array[i+1][j] - array[i][j]

            avg = round((array[i][j+1]+array[i+1][j])/2)

            maxx = abs(math.ceil((x_grad+y_grad)/2))

            if maxx < 5:
                maxx = 5

            #print(maxx)

            if avg > lim:
                
                
                add = random.randint(-maxx,0)

            elif avg < (-lim):
                add = random.randint(0,maxx)
                

            else:

                add = random.randint(-maxx,maxx)

            array[i+1][j+1] = avg + add

            #print(str(avg)+' + '+str(add)+' = '+str(array[i+1][j+1]))

        #print(array[i+1])

    return [array,size]
    
            
def show(data):

    array, size = data
    fig = plt.figure()

    ax = fig.gca(projection='3d')

    X,Y = np.mgrid[0:size:1, 0:size:1]
    Z = np.asarray(array)

    print(Z)

    ax.plot_wireframe(X,Y,Z,rstride=1, cstride=1)

    plt.show()
