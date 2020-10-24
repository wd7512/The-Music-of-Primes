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

        
        body_pos = np.where(self.game > 1)[0]

        wall_dist = []
        food_dist = []
        self_dist = []

        wall_dist.append(hx+1)
        wall_dist.append(21-hx)
        wall_dist.append(hy+1)
        wall_dist.append(21-hy)
        wall_dist.append(np.sqrt((hx+1)**2+(hy+1)**2))
        wall_dist.append(np.sqrt((hx+1)**2+(21-hy)**2))
        wall_dist.append(np.sqrt((21-hx)**2+(hy+1)**2))
        wall_dist.append(np.sqrt((21-hx)**2+(21-hy)**2))
        


        self.inputs = np.asarray(wall_dist + food_dist + self_dist,dtype = float)




a = Board()
a.add_food()
a.get_inputs()
