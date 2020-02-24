import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#random_matrix = np.random.rand(10,10)
size = 41

def new_board(size): #creates empty game board
    half = math.floor(size/2)
    board = np.zeros((size,size),dtype = int)
    board[half,half] = 1

    food_space = [random.randint(0,size-1),random.randint(0,size-1)]
    while food_space == [half,half]:
        food_space = [random.randint(0,size-1),random.randint(0,size-1)]
    board[food_space[0],food_space[1]] = -1
    
    return board
    
def add_food(board,size): # had potential to be faster
    flat = (board+0).reshape([1,size*size])
    num = np.random.choice(np.where(flat==0)[1])
    flat[0,num] = -1
    mat = flat.reshape([size,size])
    return mat

def show(frames): #frames may be the board states as a matrix
    fig = plt.figure()
    ims = []
    for frame in frames:
        im = plt.imshow(frame,animated=True)
        ims.append([im])
    ani = animation.ArtistAnimation(fig,ims,interval=100,blit=True,repeat_delay=1000)
    #ani.save('dynamic_images.gif')
    plt.show()

def test_food(no_frames,size):
    boards = [new_board(size)]
    for i in range(no_frames-1):
        new = add_food(boards[-1],size)
        boards.append(new)
    show(boards)
    return boards
    


def get_inputs(board,size):
    # 24 inputs 8 dir * distance to [wall,food,itself]
    half = math.floor(size/2)
    flat = (board+0).reshape([1,size*size])
    
    pos = np.where(board == 1)
    head_pos = (pos[0][0],pos[1][0])

    v_slice = board[:,head_pos[1]]
    h_slice = board[head_pos[0]]
    d1_slice = np.diag(board)
    d2_slice = np.diag(np.fliplr(board+0))

    print(v_slice)
    print(h_slice)
    print(d1_slice)
    print(d2_slice)
    print(board)

    def conv(halfslice):
        

    #output = [top,bot,lef,rig,top-lef,top-right,bot-right,bot-left]
    output = np.zeros((1,24))
    
    
    
    


    
