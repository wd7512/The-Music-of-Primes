import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#random_matrix = np.random.rand(10,10)


def new_board(size): #creates empty game board
    half = math.floor(size/2)
    board = np.zeros((size,size),dtype = int)
    board[half-1,half] = 2
    board[half,half] = 1
    board[half+1,half] = 1

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
    
    pos = np.where(board == 2)
    head_pos = (pos[0][0],pos[1][0])

    v_slice = board[:,head_pos[1]]
    h_slice = board[head_pos[0]]

    dif_x = half - head_pos[0]
    dif_y = half - head_pos[1]

    K = (dif_x-dif_y,-dif_y-dif_x)
    #print(K)
    d1_slice = np.diag(board,k=K[0]) #needs offsetting
    d2_slice = np.diag(np.fliplr(board+0),k=-K[1])
    '''
    print(v_slice)
    print(h_slice)
    print(d1_slice)
    print(d2_slice)
    print(board)
    '''
    vA = np.flip(v_slice[:head_pos[0]])
    vB = v_slice[head_pos[0]+1:]
    hA = np.flip(h_slice[:head_pos[1]])
    hB = h_slice[head_pos[1]+1:]

    
    
    d1A = np.flip(d1_slice[:np.where(d1_slice==2)[0][0]])
    d1B = d1_slice[np.where(d1_slice==2)[0][0]+1:] 
    d2A = np.flip(d2_slice[:np.where(d2_slice==2)[0][0]])
    d2B = d2_slice[np.where(d2_slice==2)[0][0]+1:]

    slices = [vA,d2A,hB,d1B,vB,d2B,hA,d1A]
    '''
    print(vA) 
    print(d2A)
    print(hB) 
    print(d1B) 
    print(vB)
    print(d2B)
    print(hA)
    print(d1A)
    '''

    #output = [wall dist,food dist,iteself dist]
    output = (np.zeros((1,24)))
    #print(output)
    output[0][0] = pos[0][0] + 1
    output[0][1] = math.sqrt(2) * (pos[0][0] + 1 + pos[1][0] + 1)
    output[0][2] = pos[1][0] + 1
    output[0][3] = math.sqrt(2) * (size - (pos[0][0]) + pos[1][0] + 1)
    output[0][4] = size - (pos[0][0])
    output[0][5] = math.sqrt(2) * (size - (pos[0][0]) + size - (pos[1][0]))
    output[0][6] = size - (pos[1][0])
    output[0][7] = math.sqrt(2) * (size - (pos[1][0]) + pos[0][0] + 1)

    #print(output)

    inf = 10**6

    slices_self = [np.where(var==1)[0][0]+1 if 1 in var else inf for var in slices]
    #print(slices_self)
    slices_food = [np.where(var==-1)[0][0]+1 if -1 in var else inf for var in slices]
    #print(slices_food)

    for i in range(8):
        if i%2 == 1:
            output[0][i+8] = slices_self[i] * math.sqrt(2)
        else:
            output[0][i+8] = slices_self[i]
    for i in range(8):
        if i%2 == 1:
            output[0][i+16] = slices_food[i] * math.sqrt(2)
        else:
            output[0][i+16] = slices_food[i]

    #print(output)

    return output
        
def function(x):
    return 1/(1+np.exp(-x))
    
def random_brain():
    # 24 - x - 4
    x = 24
    lay1 = np.random.rand(24,x)
    add1 = np.random.rand(1,24)
    lay2 = np.random.rand(x,4)
    add2 = np.random.rand(1,4)

    return [lay1,add1,lay2,add2]

def run_brain(brain,inputs):
    midlay = function(np.matmul(inputs,brain[0])) + brain[1]
    output = function(np.matmul(midlay,brain[2])) + brain[3]
    return output #[top, right, bot, left]

def run_game(brain):

    states = []
    
    size = 41
    board = new_board(size)
    brain = random_brain()

    moves = 200

    while moves > 0:
        moves = moves - 1
        
        inputs = get_inputs(board,size)
        outputs = run_brain(brain,inputs)
        ind_max = outputs.argmax()
        
        direc = (-1,0)
        if ind_max == 1:
            direc = (0,1)
        if ind_max == 2:
            direc = (1,0)
        if ind_max == 3:
            direc = (0,-1)

        #print(board)
        states.append(board+0)
        #print(direc)
        

        head_pos = np.where(board == 2)
        body_pos = np.where(board == 1)
        new_head_pos = (head_pos[0]+direc[0],head_pos[1]+direc[1])

        board[head_pos] = 1
        board[body_pos[0][-1],body_pos[1][-1]] = 0

        board[new_head_pos] = 2
    
        
    return states
    


'''
size = 41
a = new_board(size)
ploot = []
for i in range(100):
    ploot.append(a)
    a = add_food(a,size)
b = get_inputs(a,size)
show(ploot)
'''
show(run_game(random_brain()))
