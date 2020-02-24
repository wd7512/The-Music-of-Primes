import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def popcorn(k,j,x): #k,j tend to inf
    return (math.cos(math.factorial(k)*math.pi*x))**(2*j)

def animation(maxk,maxj,iters):
    fig = plt.figure()
    X = range(0,1000)
    X = [x/1000 for x in X]

    ims = []
    stepk = maxk/iters
    stepj = maxj/iters
    for i in range(iters):
        
        Y = [popcorn(stepk*(i+1),stepj*(i+1),x) for x in X]
        im = plt.plot(X,Y,'o')
        ims.append([im])

    ani = animation.ArtistAnimation(fig,ims,interval=50,blit=True,repeat_delay=1000)
    plt.show()

animation(100,100,10)
