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

def random_player(game):
    

    return random.choice(empty_spaces(game.board))

def min_max_player(game):
    best_score = np.NINF

    for i in range(3):
        for j in range(3):
            if game.board[i,j] == 0:
                
                test_board = np.copy(game.board)
                test_board[i,j] = game.turn

                score = minimax(test_board,game.turn)
                if score > best_score:
                    best_move = (i,j)

    return best_move
            
def minimax(board,turn): #MAKE RECURSIVE, maxing if p1, mini if p2
    possible_moves = empty_spaces(board)
    scores_of_moves = np.zeros(len(possible_moves),dtype = int)


    for i in range(len(possible_moves)):
        move = possible_moves[i]
        test_state = game()

        test_state.disp = True
        test_state.board = np.copy(board)
        test_state.turn = turn

        test_state.make_move(move)

        if test_state.end == True:
            scores_of_moves[i] = test_state.winner
        else:
            scores_of_moves[i] = minimax(test_state.board,test_state.turn)
        
    print(scores_of_moves)
    print(turn)
    if turn == 1:
        return max(scores_of_moves)
    else:
        return min(scores_of_moves)

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
