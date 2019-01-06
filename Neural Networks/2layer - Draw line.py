#2 layers
#connections, top row is input 1, bottom row input 2
import numpy as np
import random

def cleanmatrix(size):
    #size=int(input('Size of Matrix'))
    empty=''
    line=''
    for i in range(size):
        line=line+'0 '
    empty=empty+line
    for i in range(size-1):
        empty=empty+';'+line
    return np.matrix(empty)
def score(matrix): #at least 3x3 and same dimensions
    score=0
    for i in range(len(matrix)-2): #not checking edges
        for j in range(len(matrix)-2): #not checking edges
            self=matrix[i+1,j+1]

            if matrix[i,j+1]==self: #top
                score=score-1
            if matrix[i+1,j+2]==self: #top right
                score=score-1
            if matrix[i+1,j+2]==self: #right
                score=score-1
            if matrix[i+2,j+2]==self: #right bottom
                score=score-1
            if matrix[i+2,j+1]==self: #bottom
                score=score-1
            if matrix[i+2,j]==self: #bottom left
                score=score-1
            if matrix[i+1,j]==self: #left
                score=score-1
            if matrix[i,j]==self: #left top
                score=score-1

    return score

def draw(brain,size):
    matrix=cleanmatrix(size)
    for i in range(size):
        for j in 
