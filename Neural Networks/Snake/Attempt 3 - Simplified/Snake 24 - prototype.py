import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Brain: #generates random brain
    def __init__(self):
        # just inputs and outputs
        self.weights = np.random.randn(24,4)
        self.biases = np.zeros((1,4))

    def calc(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

    def mutate(self):
        self.weights = self.weights + 0.01 * np.random.randn(24,4)
        self.biases = self.biases + 0.1 * np.random.randn(1,4)


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


        while self.game[food_pos[0]][food_pos[1]] != 0:
            food_pos = [np.random.randint(0,self.size),np.random.randint(0,self.size)]

        self.game[food_pos] = -10

    def get_inputs(self):
        
        head_pos = np.argwhere(self.game == 1)[0]


        hx = head_pos[0]
        hy = head_pos[1]

        food_pos = np.where(self.game == -10)
        fx = food_pos[0]
        fy = food_pos[1]

        body_pos = np.where(self.game > 1)
        list_body_pos = list(zip(body_pos))
        

        wall_dist = []
        food_dist = [0,0,0,0,0,0,0,0]
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

        try:
            if hx == fx:
                pass
        except:
            print(hx)
            print(fx)


        if hx == fx: #if horizontal plane
            if hy < fy:
                food_dist[0] = fy - hy
            else:
                food_dist[1] = hy - fy

        if hy == fy: #if vertical plane
            if hx < fx:
                food_dist[2] = fx - hx
            else:
                food_dist[3] = hx - fx


        if hx + hy == fx + fy: #is non-leading diag
            if hy < fy:
                food_dist[4] = (fy - hy)*np.sqrt(2)
            else:
                food_dist[5] = (hy - fy)*np.sqrt(2)

        if hx - fx == hy - fy: #leading diag
            if hy < fy:
                food_dist[6] = (fy - hy)*np.sqrt(2)
            else:
                food_dist[7] = (hy - fy)*np.sqrt(2)


        for pos in list_body_pos:

            #print(pos)
            #print(self.game)
            
            fx = pos[0][1] #swaped, might be wrong but seemed to be flipped
            fy = pos[0][0]
            

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
                if hy < fy:
                    if fy - hy < self_dist[6] or self_dist[6] == 0:
                        self_dist[6] = (fy - hy)*np.sqrt(2)
                else:
                    if hy - fy < self_dist[7] or self_dist[7] == 0:
                        self_dist[7] = (hy - fy)*np.sqrt(2)


            
        

        
        max_dist = [self.size,self.size,self.size,self.size,
                    self.size*np.sqrt(2),self.size*np.sqrt(2),self.size*np.sqrt(2),self.size*np.sqrt(2)]

        tot_dist = np.asarray(max_dist + max_dist + max_dist)
                    
        
        # need to invert output

        self.inputs = tot_dist - np.asarray(wall_dist + food_dist + self_dist,dtype = float)


    def run(self,brain):

        self.old_start = np.copy(self.game)

        self.past_states = []


        moves = 100
        self.score = 0

        while moves > 0:

            moves = moves - 1
            self.score = self.score + 1

            self.get_inputs()
            brain.calc(self.inputs)

            output = brain.output
            ind_max = output.argmax()

            direc = (-1,0) #if 0, just saves an if statement
            if ind_max == 1:
                direc = (0,1)
            if ind_max == 2:
                direc = (1,0)
            if ind_max == 3:
                direc = (0,-1)

            self.past_states.append(np.copy(self.game))

            head_pos = np.where(self.game == 1)
            body_pos = np.where(self.game > 1)
            list_body_pos = list(zip(body_pos[0],body_pos[1]))
            snake_len = len(body_pos[0])

            new_head_pos = (head_pos[0][0]+direc[0],head_pos[1][0]+direc[1])


 

            on_itself = False

            for pos in list_body_pos:

                
                if new_head_pos == (pos[0],pos[1]):
     
                    on_itself = True


            if -1 == new_head_pos[0] or -1 == new_head_pos[1] or self.size == new_head_pos[0] or self.size == new_head_pos[1] or on_itself == True:
                moves = -1
            else:
                food_pos = np.where(self.game == -10)


                self.game[body_pos] = self.game[body_pos] + 1
                self.game[head_pos] = self.game[head_pos] + 1
                self.game[new_head_pos] = 1

                
                if new_head_pos == (food_pos[0],food_pos[1]):
                    
                    moves = moves + 100
                    self.score = self.score + 10
                    board = self.add_food()
                    
                else:
                    self.game[np.where(self.game == (snake_len+2))] = 0

    def reset(self):
        self.game = np.copy(self.old_start)


def show(frames): #frames may be the board states as a matrix
    fig = plt.figure()
    ims = []
    for frame in frames:
        im = plt.imshow(frame,animated=True)
        ims.append([im])
    ani = animation.ArtistAnimation(fig,ims,interval=50,blit=True,repeat_delay=1000)
    #ani.save('dynamic_images.gif')
    plt.show()

def simple_sim(Pop,Gens):

    repeat = 5

    top_percent = 0.2
    rand_percent = 0.1
    
    rand_num = int(Pop * rand_percent)
    

    

    brains = [Brain() for i in range(Pop)]
    scores = np.zeros((Gens,Pop))

    for i in range(Gens):

        score = np.zeros((1,Pop),dtype = int)[0]
        
        
        for j in range(repeat):

            original = Board() #the start
            original.add_food()
            
            
            for k in range(Pop):

                brain = brains[k]
                original.run(brain)



                score[k] = original.score + score[k]

                original.reset()


        #need proper function to get top 20

        score_ind = sorted(np.copy(score))


        min_max = score_ind[-int(Pop * top_percent)]

        tops = np.argwhere(score > min_max)
        top_brains = [brains[int(i)] for i in tops]

        top_num = len(score[tops])
        child_num = Pop - top_num - rand_num
        
        top_child_ratio = int(np.floor(child_num / top_num))
        remainder = int(child_num - top_child_ratio * top_num)
        
        random_brains = [Brain() for i in range(rand_num)]

        
        

        
        child_brains = []

        for top in top_brains:
            for i in range(top_child_ratio):
                child = Brain()
                
                child.weights = top.weights
                child.biases = top.biases

                child.mutate()
                
                child_brains.append(child)

        best_score = score_ind[-1]
        
        best_ind = np.argwhere(score == best_score)[0]
        best_brain = brains[int(best_ind)]
        

        for i in range(remainder):
            top = best_brain

            child = Brain()
                
            child.weights = top.weights
            child.biases = top.biases

            child.mutate()
                
            child_brains.append(child)


        print('Best Score: '+str(best_score))
        print('Top Scoes:  '+str(list(score[tops])))
        

        brains = random_brains + top_brains + child_brains

        print('Population: '+str(len(brains)))
        
            

            

    return score

        
                
                
                
                

        
        
    


a = simple_sim(100,10)
