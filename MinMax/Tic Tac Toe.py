#tic tac toe game
import numpy as np
import random
import matplotlib.pyplot as plt



def is_win(arr):
    if min(arr) == max(arr) and arr[0] != 0:
        return True
    else:
        return False

class game:
    def __init__(self):
        self.board = np.zeros([3,3],dtype = int)
        self.turn = 1
        self.winner = 0
        self.end = False
        self.disp = False


    def next_turn(self):
        if self.turn == 1:
            self.turn = -1
        else:
            self.turn = 1


    def make_move(self,pos):

        if self.disp == True:
            print(pos)
        
        if type(pos) != tuple or self.board[pos] != 0 or self.winner != 0:
            print('invalid input or game is over')
        else:
            self.board[pos] = self.turn

            all_lines = [self.board[0,:],
                         self.board[1,:],
                         self.board[2,:],
                         self.board[:,0],
                         self.board[:,1],
                         self.board[:,2],
                         [self.board[(0,0)],self.board[(1,1)],self.board[(2,2)]],
                         [self.board[(0,2)],self.board[(1,1)],self.board[(2,0)]]
                ]

            if self.disp == True:
                print(str(self.board) + '\n')

            if any([is_win(boole) for boole in all_lines]) == True:
                self.winner = self.turn
                self.end = True

                if self.disp == True:
                    print(str(self.winner) + ' is the winner')

            if 0 not in self.board:
                self.end = True

                if self.disp == True:
                    print('Draw')

            self.next_turn()


def empty_spaces(board):
    spaces = []
    for i in range(3):
        for j in range(3):
            if board[i,j] == 0:
                spaces.append((i,j))

    return spaces

def possible_states(moves,board,turn):
    states = []
    for move in moves:
        new_state = np.copy(board)
        new_state[move] = turn
        states.append(new_state)

    return states

def random_player(game):

    return random.choice(empty_spaces(game.board))

def min_max_player(game):
    if game.turn == 1:
        ismax = True
        best_score = np.NINF

        possible_moves = empty_spaces(game.board)


        
        
    else:
        ismax = False
        best_score = np.Inf

    

    



    return best_move
            


def run_game(p1,p2):
    a = game()
    a.disp = True
    while a.end == False:
        if a.turn == 1:
            func = p1
        else:
            func = p2

        move = func(a)
        a.make_move(move)

    return a.winner

out = []
for i in range(1):

    out.append(run_game(min_max_player,random_player))

plt.hist(out)
plt.show()
