import numpy as np
import matplotlib.pyplot as plt

class Random_Brain: #generates random brain
    def __init__(self):
        # just inputs and outputs
        self.weights = 0.1 * np.random.randn(24,4)
        self.biases = np.zeros((1,4))

    def calc(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases


class Board:
    def __init__(self):
        self.size = 21
        self.half = int(np.floor(self.size/2))
        
        board = np.zeros((self.size,self.size),dtype = int)
        board[self.half-1,self.half] = 1
        board[self.half,self.half] = 2
        board[self.half+1,self.half] = 3
        self.game = board

    def add_food(self):
        food_pos = (np.random.randint(0,self.size),np.random.randint(0,self.size))
        while self.game[food_pos] != 0:
            food_pos = [np.random.randint(0,self.size),np.random.randint(0,self.size)]
        self.game[food_pos] = -10

    def get_inputs(self):
        
        head_pos = np.where(self.game == 1)

        hx = head_pos[0]
        hy = head_pos[1]

        food_pos = np.where(self.game == -10)
        fx = food_pos[0]
        fy = food_pos[1]

        body_pos = np.where(self.game > 1)
        

        wall_dist = []
        food_dist = [0,0,0,0]
        self_dist = [0,0,0,0,0,0,0,0]

        wall_dist.append(hx+1)
        wall_dist.append(21-hx)
        wall_dist.append(hy+1)
        wall_dist.append(21-hy)
        wall_dist.append(np.sqrt((hx+1)**2+(hy+1)**2))
        wall_dist.append(np.sqrt((hx+1)**2+(21-hy)**2))
        wall_dist.append(np.sqrt((21-hx)**2+(hy+1)**2))
        wall_dist.append(np.sqrt((21-hx)**2+(21-hy)**2))

        
        # output = [horizontal,vertical,non-leading,leading]
        
        #bottom left to top right must add to the same
        #leading diag must scale do diff in x = diff in y
        
        #horizontal first

        if hx == fx: #if horizontal plane
            if hy < fy:
                food_dist[0] = fy - hy
            else:
                food_dist[0] = hy - fy

        if hy == fy: #if vertical plane
            if hx < fx:
                food_dist[1] = fx - hx
            else:
                food_dist[1] = hx - fx


        if hx + hy == fx + fy: #is non-leading diag
            if hy < fy:
                food_dist[2] = (fy - hy)*np.sqrt(2)
            else:
                food_dist[2] = (hy - fy)*np.sqrt(2)

        if hx - fx == hy - fy: #leading diag
            if hy < fy:
                food_dist[2] = (fy - hy)*np.sqrt(2)
            else:
                food_dist[2] = (hy - fy)*np.sqrt(2)


        for pos in body_pos:
            fx = pos[1] #swap? might be wrong but seemed to be flipped
            fy = pos[0]
            

            if hx == fx: #if horizontal plane
                if hy < fy:
                    if fy - hy < self_dist[0] or self_dist[0] == 0:
                        self_dist[0] = fy - hy
                else:
                    if hy - fy < self_dist[1] or self_dist[1] == 0:
                        self_dist[1] = hy - fy

            if hy == fy: #if vertical plane
                if hx < fx:
                    if fx - hx < self_dist[2] or self_dist[2] == 0:
                        self_dist[2] = fx - hx
                else:
                    if hx - fx < self_dist[3] or self_dist[3] == 0:
                        self_dist[3] = hx - fx

            
            if hx + hy == fx + fy: #is non-leading diag
                if hy < fy:
                    if fy - hy < self_dist[4] or self_dist[4] == 0:
                        self_dist[4] = (fy - hy)*np.sqrt(2)
                else:
                    if hy - fy < self_dist[5] or self_dist[5] == 0:
                        self_dist[5] = (hy - fy)*np.sqrt(2)

            if hx - fx == hy - fy: #leading diag
                print('ok')
                if hy < fy:
                    if fy - hy < self_dist[6] or self_dist[6] == 0:
                        self_dist[6] = (fy - hy)*np.sqrt(2)
                else:
                    if hy - fy < self_dist[7] or self_dist[7] == 0:
                        self_dist[7] = (hy - fy)*np.sqrt(2)


            
        

        
        
        
        # need to invert output

        self.inputs = np.asarray(wall_dist + food_dist + self_dist,dtype = float)




a = Board()
a.add_food()
a.get_inputs()
print(a.inputs)
plt.matshow(a.game)
plt.show()
