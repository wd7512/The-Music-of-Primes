import random
import matplotlib.pyplot as plt

buyers=[50]
sellers=[30]

buygraph=[]
sellgraph=[]
for i in range(len(buyers)):
    buygraph.append([buyers[i]])
    sellgraph.append([seller[i]])

def round(buyers,sellers):
    order=[]
    for i in range(len(buyers)):
        order.append(i)
    random.shuffle(order)
