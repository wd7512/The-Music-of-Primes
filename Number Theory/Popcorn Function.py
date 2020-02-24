import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import math


def popcorn(k,j,x): #k,j tend to inf
    return (math.cos(math.factorial(k)*math.pi*x))**(2*j)

def animat(maxk,maxj,iters):
    fig = plt.figure()
    X = range(0,1000)
    X = [x/1000 for x in X]

    ims = []
    stepk = maxk/iters
    stepj = maxj/iters
    for i in range(iters):
        
        Y = [popcorn(stepk*(i+1),stepj*(i+1),x) for x in X]
        im, = plt.plot(X,Y,'ro')
        ims.append([im])

    print(ims)

    ani = animation.ArtistAnimation(fig,ims,interval=200,repeat_delay=1000)
    plt.show()


fig, ax = plt.subplots()
X = [np.random.rand() for i in range(1000)]
k = 1
j = 1
Y = [popcorn(k,j,x) for x in X]
l, = plt.plot(X,Y,'bo')
ax.margins(x=0)
axk = plt.axes([0.25, 0.1, 0.65, 0.03])
axj = plt.axes([0.25, 0.1, 0.65, 0.03])

def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(popcorn(k,j,X))
    fig.canvas.draw_idle()
