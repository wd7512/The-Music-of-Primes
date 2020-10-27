import networkx as nx
import numpy as np
import os
import matplotlib.pyplot as plt

textfiles = [f for f in os.listdir() if f[-4:] == '.txt']
tot = len(textfiles)

G = nx.DiGraph()
for i in range(tot):
    f = open(textfiles[i],'r')
    data = f.readlines()
    f.close()
    #print(data)
    if data == []:
        #G.add_node(i)
        G.add_node(textfiles[i][:-4])
    else:
        for person in data:
            #G.add_edge(i,textfiles.index(person[:-1]+'.txt'))
            G.add_edge(textfiles[i][:-4],person)


#pos = nx.circular_layout(G)
pos = nx.kamada_kawai_layout(G)
#pos = nx.spring_layout(G,iterations=1000)
nx.draw_networkx(G)
plt.show()

