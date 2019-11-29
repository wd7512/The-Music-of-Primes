import random
import matplotlib.pyplot as plt
import numpy as np

def random_picture(length,size):
    picture = []
    for i in range(length):
        square = np.random.rand(size,size)
        picture.append(square)

    return picture

def show(arraylist):
    for pic in arraylist:
        plt.matshow(pic)
        plt.show()

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

def get_inputs(arraylist): #gets left and right border averages
    output = []
    for item in arraylist:
        score_left = 0
        score_right = 0
        for row in item:
            score_left = score_left + row[0]
            score_right = score_right + row[-1]
        output.append(score_left)
        output.append(score_right)
    return output            

def random_matricies(length): #creates random brain
    
    sizes = ((length*2),25,length) # these are the variables
    weight_sizes = [(a,b) for a,b in zip(sizes[:-1],sizes[1:])]
    weights = [np.random.standard_normal(s) for s in weight_sizes]
    #print(weights)
    biases = [np.random.standard_normal((1,s)) for s in sizes[1:]]
    #print(biases)
    return [weights,biases]

def function(x):
    return 1/(1+np.exp(-x))

def run_brain(brain,inputs): # given inputs, the brain calculates outputs
    weights = brain[0]
    biases = brain[1]

    layer1 = function(np.matmul(inputs,weights[0])+biases[0])
    output = function(np.matmul(layer1,weights[1])+biases[1])
    return output

def rearrange_decoder(picture,output): # decodes and rearranges pictue, given the ouput
    outlist = (np.ndarray.tolist(output))[0]
    newpicture = []
    for i in range(len(picture)):
        maxx = outlist.index(max(outlist))
        newpicture.append(picture[maxx])
        outlist[maxx] = -1

    return newpicture

        
