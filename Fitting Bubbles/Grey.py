from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt

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
        coords = (random.randint(0,dim[0]),random.randint(0,dim[1]))
        
        rad = round(abs(np.random.normal() * (min_dim/2)))

        
        col = np.random.normal() * 100
        bubble = [coords,rad,col]
        bubbles.append(bubble)

    return bubbles


def calc(bubbles,dim):
    

    canvas = np.zeros(dim)

    print('calculating circles')
    for bubble in bubbles:
        coords = bubble[0]
        rad = bubble[1]
        col = bubble[2]

        
        corner = (coords[0]-rad-1,coords[1]-rad-1)
        for i in range(rad*2+1):
            for j in range(rad*2+1):
                dist = (i-(rad+1))**2 + (j-(rad+1))**2
                if dist < rad+1:

                    write_coord = (corner[0]+i,corner[1]+j)
                    if write_coord[0] >= 0 and write_coord[1] >= 0:
                        if write_coord[0] < dim[0] and write_coord[1] < dim[1]:
                            canvas[write_coord] = canvas[write_coord] + col
                
        
        

        
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
    
    
dim = (100,100)
goal = line(100)

a = calc(random_bubbles(30,dim),dim)


diff(a,goal)

