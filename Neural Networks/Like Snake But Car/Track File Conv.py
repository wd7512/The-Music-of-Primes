import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Brain: #generates random brain
    def __init__(self):
        # just inputs and outputs
        self.weights = np.random.randn(8,4)
        self.biases = np.zeros((1,4))

    def calc(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

    def mutate(self):
        self.weights = self.weights + 0.01 * np.random.randn(24,4)
        #self.biases = self.biases + 0.1 * np.random.randn(1,4)

#maybe need activation function


def show_ani(frames): #frames may be the board states as a matrix
    fig = plt.figure()
    ims = []
    for frame in frames:
        im = plt.imshow(frame,animated=True)
        ims.append([im])
    ani = animation.ArtistAnimation(fig,ims,interval=50,blit=True,repeat_delay=1000)
    #ani.save('dynamic_images.gif')
    plt.show()


def save_track():
    pass

track = np.zeros((300,300),dtype = int)

np.savetxt('track.csv',track,delimiter=',',fmt='%i')
