import random
import matplotlib.pyplot as plt
import numpy as np

def random_picture(length,size):
    picture = []
    for i in range(length):
        square = np.random.rand(size,size)
        picture.append(square)

    return picture

def combine(arraylist): #combines arraylist into full picture
    length = len(arraylist)
    size = len(arraylist[0])
    newsize = (size,size*length)
    output = np.zeros(newsize)
    
    for k in range(length):
        sq = arraylist[k]
        for i in range(size):
            for j in range(size):
                output[i][j+k*size] = sq[i][j]

    return output

def test(arraylist): #gives score from 0-1
    length = len(arraylist)
    size = len(arraylist[0])

    sumscore = 0

    for i in range(length-1):
        sq1 = arraylist[i]
        sq2 = arraylist[i+1]
        bdr1 = []
        bdr2 = []
        for row in sq1:
            bdr1.append(row[-1])
        for row in sq2:
            bdr2.append(row[0])

        for i in range(size):
            sumscore = sumscore + abs(bdr1[i]-bdr2[i])

        score = sumscore / (length-1)

        return score
