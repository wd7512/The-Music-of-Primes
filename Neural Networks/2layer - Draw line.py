#2 layers
#connections, top row is input 1, bottom row input 2
import numpy as np
import random
def score(matrix): #at least 3x3 and same dimensions
    score=0
    for i in range(len(matrix)-2): #not checking edges
        for j in range(len(matrix)-2): #not checking edges
            self=matrix[1+i,1+j]
            
