from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import os
import glob

def grey(pic_name,file_type):
    picture_name = pic_name+file_type
    img = Image.open(picture_name).convert('LA')
    print('dim - '+str(np.size(img)))
    name = pic_name+'-grey.png'
    print(name+' saved')
    img.save(name)

def startup(pic_name):
    file_name = pic_name + '.png'
    img = Image.open(file_name)
    dim = np.size(img)

def random_bubbles(num,dim):
    print('getting random canvas')
    min_dim = min(dim)

    bubbles = []
    for i in range(num):
        coords = (random.randint(0,dim[0]-1),random.randint(0,dim[1]-1))
        
        rad = round((abs(np.random.normal() * (min_dim/8))))
        
        col = np.random.normal() * 100
        bubble = [coords,rad,col]
        bubbles.append(bubble)

    return bubbles


def calc(bubbles,dim):
    

    canvas = np.zeros(dim)

    print('calculating circles')
    for bubble in bubbles:
        coords = bubble[0]

        #print(coords)
        
        Y = coords[0]
        X = coords[1]

        rad = bubble[1]
        #print(rad)
        col = bubble[2]
        #print(col)
        
        X_max = min(X+rad+1,dim[1])
        X_min = max(X-rad,0)
        Y_max = min(Y+rad+1,dim[0])
        Y_min = max(Y-rad,0)
        
        

        '''
        corner = (Y-rad-1,X-rad-1)
        for i in range(rad*2+1):
            for j in range(rad*2+1):
                dist = (i-(rad+1))**2 + (j-(rad+1))**2
                if dist < rad+1:

                    write_coord = (corner[0]+i,corner[1]+j)
                    if write_coord[0] >= 0 and write_coord[1] >= 0:
                        if write_coord[0] < dim[0] and write_coord[1] < dim[1]:
                            canvas[write_coord] = canvas[write_coord] + col

        '''


        
        
        canvas[Y][X_min:X_max] = canvas[Y][X_min:X_max] + col
        canvas[Y_min:Y_max,X] = canvas[Y_min:Y_max,X] + col

        canvas[coords] = canvas[coords] - col

        quarter_coords = []
        num = (rad+1)**2
        for i in range(rad+1):
            i_sq = (i+1)**2

            
            for j in range(rad):
                if i_sq + (j+1)**2 < num:
                   quarter_coords.append([i+1,j+1])

    
        Q1_coords = [[Y-c[0],X-c[1]] for c in quarter_coords if Y-c[0] >= 0 and X-c[1] >= 0 and Y-c[0] < dim[0] and X-c[1] < dim[1]]
        Q2_coords = [[Y-c[0],X+c[1]] for c in quarter_coords if Y-c[0] >= 0 and X+c[1] >= 0 and Y-c[0] < dim[0] and X+c[1] < dim[1]]
        Q3_coords = [[Y+c[0],X+c[1]] for c in quarter_coords if Y+c[0] >= 0 and X+c[1] >= 0 and Y+c[0] < dim[0] and X+c[1] < dim[1]]
        Q4_coords = [[Y+c[0],X-c[1]] for c in quarter_coords if Y+c[0] >= 0 and X-c[1] >= 0 and Y+c[0] < dim[0] and X-c[1] < dim[1]]


        tot_coords = Q1_coords + Q2_coords + Q3_coords + Q4_coords
        for c in tot_coords:

            canvas[c[0]][c[1]] = canvas[c[0]][c[1]] + col
                    



                
        
        

        
    print('zeroing negatives')
    zero = lambda i : 0 if i<0 else i
    fun = np.vectorize(zero)
    canvas = fun(canvas)

    return canvas

def show(canvas):

    plt.imshow(canvas,cmap = 'gray',vmin = 0,vmax = 255)
    plt.colorbar()
    plt.show()

def random_test():
    dim = (200,200)
    a = random_bubbles(500,dim)
    show(calc(a,dim))

def line(square_dim):
    dim = square_dim
    output = np.zeros((dim,dim))


    div = 4
    width = int(dim/4)
    for i in range(div):
        
        if i%2 == 0:
            new_i = i * width
            output[new_i:new_i + width] = 255

    return output



def diff(canvas,goal):
    if np.shape(canvas) != np.shape(goal):
        print('wrong dim of goal')

    dim = np.shape(canvas)
    worst = 255 * dim[0] * dim[1]

    dif = abs(canvas - goal)
    score = dif.sum()

    percent = score / worst * 100
    print('percent correct = '+str(percent))
    return percent
    

def timer_calc(dims,bub_nums):

    

    for dim in dims:
        for bub_num in bub_nums:
            timer_nums = []
            for i in range(100):
                print(i)
                tic = time.perf_counter()
                a = calc(random_bubbles(bub_num,(dim,dim)),(dim,dim))
                toc = time.perf_counter()
                timer_nums.append(toc-tic)

            name = 'dim'+str(dim)+' bubs'+str(bub_num)+'.txt'
            with open(name,'w') as f:
                for t in timer_nums:
                    f.write(str(t)+'\n')


def timer_show(dims,bub_nums):



    avg_dims = []
    for dim in dims:
        avg_dim = []
        for bub_num in bub_nums:
            name = 'dim'+str(dim)+' bubs'+str(bub_num)+'.txt'
            with open(name,'r') as f:
                data = f.readlines()
            data = [float(a) for a in data]

            avg = sum(data)/len(data)
            avg_dim.append(avg)

        avg_dims.append(avg_dim)

    for i in range(len(bub_nums)):
        Y = avg_dims[i]
        try:
            plt.plot(dims,Y,label = str(bub_nums[i]) + 'bubbles')
        except ValueError:
            print(dims)
            print(Y)
            print(avg_dims)
            print(bub_nums)
            a = input('look')

    plt.legend()
    plt.xlabel('Dims')
    plt.ylabel('Avg Time')
    plt.show()
    
def timer_clear():
    for filename in glob.glob('dim*'):
        os.remove(filename)

def timer_test():

    timer_clear()
    dims = [10,20,30,40,50,60,70,80,90,100]
    bub_nums = list(range(10,100,10))
    timer_calc(dims,bub_nums)

    timer_show(dims,bub_nums)


timer_test()



