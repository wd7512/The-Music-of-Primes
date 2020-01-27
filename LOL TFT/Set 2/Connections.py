import turtle
import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
f = open('Traits.csv','r')
traits_raw = f.readlines()[1:]
f.close()
traits = []
for t in traits_raw:
    traits.append(t.split(',')[0])

traits = list(set(traits))

f = open('Champs - No LuxQi.csv','r')
champs_raw = f.readlines()[1:]
f.close()
champs = []
for c in champs_raw:
    c = c.split(',')
    add = [c[0]]+c[-3:]
    if add[-1] == '\n':
        add = add[:-1]
    else:
        add[-1] = add[-1][:-1]
    champs.append(add)



def simple(champs):
    tot = len(champs)
    print(tot)
    G = nx.Graph()
    for i in range(tot):
        G.add_node(champs[i][0])

    for i in range(tot):
        for j in range(tot):
            if i != j:
                c1 = champs[i]
                c2 = champs[j]
                #print(set(c1) & set(c2))
                num = len(set(c1[1:]) & set(c2[1:]))
                #print(num)
                
                for x in range(num):
                    G.add_edge(c1[0],c2[0])
                    
    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx(G,pos)
    plt.show()

def trait_nodes(champs,traits):
    traits.remove('Avatar')

    
    tot = len(champs)
    print(tot)
    G = nx.Graph()
    
    for t in traits:
        G.add_node(t)
    
    for c in champs:
        G.add_node(c[0])
        for t in c[1:]:
            #print(c[0]+' '+t)
            G.add_edge(c[0],t)
    
    print(str(G.number_of_edges())+' edges')
    print(str(G.number_of_nodes())+' nodes')

    
    #pos = nx.kamada_kawai_layout(G)
    pos = nx.spring_layout(G,iterations=10000)
    nx.draw_networkx(G,pos)
    plt.show()

    return nx.to_numpy_matrix(G)
            
#simple(champs)
A = trait_nodes(champs,traits)

    
