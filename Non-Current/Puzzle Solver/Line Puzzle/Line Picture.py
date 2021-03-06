import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from google_images_download import google_images_download
import os
import math

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

def grey(picture_name):
    img = Image.open(picture_name).convert('LA')
    print('dim - '+str(np.size(img)))
    name = picture_name+'-grey.png'
    print(name+' saved')
    img.save(name)

def downloadimages(query):
    response = google_images_download.googleimagesdownload()  
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":100, 
                 "print_urls":True, 
                 "size": "large", 
                 "aspect_ratio": "panoramic"}
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit":4, 
                     "print_urls":True,  
                     "size": "medium"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass

def grey_folder(folder):
    images = [name for name in os.listdir(folder)]
    print(images)
    for im in images:
        newname = folder + '/' +im
        grey(newname)

def array(picture_name): #input greyscale picture
    img = Image.open(picture_name)
    size = np.size(img)
    #print(size)
    data = list(img.getdata())
    #print(len(data))
    #print(np.size(data))
    arraydata = np.zeros((size[1],size[0]))
    for i in range(size[1]):
        ind = i*size[0]
        #print(ind)
        for j in range(size[0]):
            arraydata[i][j] = data[ind+j][0]

    return arraydata

def slice_array(slice_size,array):
    shape = np.shape(array)
    num1 = math.floor(shape[0]/slice_size)
    num2 = math.floor(shape[1]/slice_size)
    slices = []
    for i in range(num1):
        start = i * slice_size
        slise = np.zeros((slice_size,slice_size * num2))
        for j in range(slice_size):
            for k in range(slice_size * num2):
                slise[j][k] = array[start+j][k]
        slices.append(slise)

    return slices

def save_image(array,name):
    im = Image.fromarray(array)
    
    im.save(name)

def test_slice():

    arra = array('horse.jpg-grey.png')
    slices = slice_array(50,arra)
    for slik in slices:
        plt.matshow(slik)
        plt.colorbar()
        plt.show()
        
            
    
