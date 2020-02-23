import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#random_matrix = np.random.rand(10,10)

def new_board(size): #creates empty game board
    half = math.floor(size/2)
    board = np.zeros((size,size),dtype = int)
    board[half,half] = 1

    food_space = [random.randint(0,size-1),random.randint(0,size-1)]
    while food_space == [half,half]:
        food_space = [random.randint(0,size-1),random.randint(0,size-1)]
    board[food_space[0],food_space[1]] = 2
    
    return board
    
def add_food(board,size):
    flat = board.reshape([1,size*size])
    num = np.random.choice(np.where(flat==0)[1])
    flat[0,num] = 2
    mat = flat.reshape([size,size])
    return mat

def show(frames): #frames may be the board states as a matrix
    fig = plt.figure()
    ims = []
    for frame in frames:
        im = plt.imshow(frame,animated=True)
        ims.append([im])
    ani = animation.ArtistAnimation(fig,ims,interval=100,blit=True,repeat_delay=100)
    # ani.save('dynamic_images.mp4')
    plt.show()

