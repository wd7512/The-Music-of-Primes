import numpy as np
import random

def empty_board():
    return np.zeros([3,3], dtype=int)

def game_over(board):

    
    
    all_lines = [
        board[0,:],
        board[1,:],
        board[2,:],
        board[:,0],
        board[:,1],
        board[:,2],
        [board[(0,0)],board[(1,1)],board[(2,2)]],
        [board[(2,0)],board[(1,1)],board[(0,2)]]
    ]

    for line in all_lines:
        if min(line) == max(line) and line[0] != 0:
            return line[0]

    if len(empty_spaces(board)) == 0:
        return 0

    return False

def run_game(player1,player2): #players are functions
    turn = np.random.choice([1,-1])

    board = empty_board()

    while type(game_over(board)) == bool:
        if turn == 1:
            move = player1(board,True)
        else:
            move = player2(board,False)

        board[move] = turn

        if turn == 1:
            turn = -1
        else:
            turn = 1

        print(board)

    print(game_over(board),'Wins')

    

def random_player(board,ismax):
    return random.choice(empty_spaces(board))

def empty_spaces(board):
    spaces = []
    for i in range(3):
        for j in range(3):
            if board[i,j] == 0:
                spaces.append((i,j))

    return spaces

def min_max(board,ismax):
    state = game_over(board)
    possible_moves = empty_spaces(board)

    if type(state) == bool:
        if ismax == True: #best move for player 1
            scores = []
            for move in possible_moves:
                virtual_state = np.copy(board)
                virtual_state[(move)] = 1
                scores.append(min_max(virtual_state,not ismax))

            print(scores)

            return max(scores)
        else: #best move for player 2
            scores = []
            for move in possible_moves:
                virtual_state = np.copy(board)
                virtual_state[(move)] = -1
                scores.append(min_max(virtual_state,not ismax))

            print(scores)
            return min(scores)
        
    else:
        return state

def min_max_player(board,ismax):
    possible_moves = empty_spaces(board)
    
    if ismax == True:
        best_score = np.NINF
        for move in possible_moves:
            test_board = np.copy(board)
            test_board[move] = 1
            score = min_max(test_board,ismax)

            if score > best_score:
                best_move = move

    
    else:
        best_score = np.Inf
        for move in possible_moves:
            test_board = np.copy(board)
            test_board[move] = -1
            score = min_max(test_board,ismax)

            if score < best_score:
                best_move = move

    return best_move


a = empty_board()
a[(1,1)] = 1
a[(0,0)] = -1
a[(0,1)] = 1
print(a)

print(min_max(a,True))