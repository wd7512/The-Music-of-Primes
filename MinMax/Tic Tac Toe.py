#tic tac toe game
import numpy as np

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


    def next_turn(self):
        if self.turn == 1:
            self.turn = -1
        else:
            self.turn = 1


    def make_move(self,pos):
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

            if any([is_win(boole) for boole in all_lines]) == True:
                self.winner = self.turn
                print(str(self.winner) + 'is the winner')

            self.next_turn()

        print(self.board)

