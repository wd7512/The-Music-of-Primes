import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#make iterative

fig, axs = plt.subplots(2, 2)


img = mpimg.imread('Track 1.jpg')
axs[0,0].imshow(img,cmap = 'Greys')
data = np.asarray(img)
var = np.shape(data)



new_data = np.zeros((var[0],var[1]),dtype = int)

for i in range(var[0]):
    for j in range(var[1]):

        vara = sum(data[i][j])
        if vara == 459:
            
            new_data[i][j] = 1

axs[1,0].imshow(new_data,cmap = 'Greys')

data = np.copy(new_data)

new_data = np.zeros((var[0],var[1]),dtype = int)

next_to = [[1,-1],[1,0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]]

for i in range(var[0]):
    for j in range(var[1]):
        tiles = [0,1,2,3,4,5,6,7]
        if i == 0:
            tiles.remove(5)
            tiles.remove(6)
            tiles.remove(7)
        if j == 0:
            tiles.remove(0)
            tiles.remove(3)
            if 5 in tiles: tiles.remove(5)
        if i == var[0] - 1:
            if 0 in tiles: tiles.remove(0)
            tiles.remove(1)
            tiles.remove(2)
        if j == var[1] - 1:
            if 2 in tiles: tiles.remove(2)
            tiles.remove(4)
            if 7 in tiles: tiles.remove(7)

        count = 0

        for n in tiles:

            pos = (i+next_to[n][0],j+next_to[n][1])
        
            count = count + data[pos]
        

        if count > 1:
            new_data[i][j] = 1

axs[0,1].imshow(new_data,cmap = 'Greys')
data = np.copy(new_data)

new_data = np.zeros((var[0],var[1]),dtype = int)

next_to = [[1,-1],[1,0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]]

for i in range(var[0]):
    for j in range(var[1]):
        tiles = [0,1,2,3,4,5,6,7]
        if i == 0:
            tiles.remove(5)
            tiles.remove(6)
            tiles.remove(7)
        if j == 0:
            tiles.remove(0)
            tiles.remove(3)
            if 5 in tiles: tiles.remove(5)
        if i == var[0] - 1:
            if 0 in tiles: tiles.remove(0)
            tiles.remove(1)
            tiles.remove(2)
        if j == var[1] - 1:
            if 2 in tiles: tiles.remove(2)
            tiles.remove(4)
            if 7 in tiles: tiles.remove(7)

        count = 0

        for n in tiles:

            pos = (i+next_to[n][0],j+next_to[n][1])
        
            count = count + data[pos]
        

        if count > 1:
            new_data[i][j] = 1

axs[1,1].imshow(new_data,cmap = 'Greys')

plt.show()
