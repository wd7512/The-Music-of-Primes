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

f = open('Champs.csv','r')
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


    
    tot = len(champs)
    print(tot)
    G = nx.Graph()

    colour_map = []
    
    for t in traits:
        G.add_node(t)
        colour_map.append('green')
        #print(str(t) + ' blue')
    
    for c in champs:
        G.add_node(c[0])
        colour_map.append('yellow')
        #print(str(c[0])+ ' green')
        for t in c[1:]:
            #print(c[0]+' '+t)
            G.add_edge(c[0],t,length = 1)




    #pos = nx.kamada_kawai_layout(G)
    #pos = nx.spring_layout(G)
    nx.draw_networkx(G,node_color=colour_map)
    #nx.draw(G,node_color = colour_map)
    plt.show()

    return [nx.to_numpy_matrix(G,nodelist=traits+[c[0] for c in champs]),traits]
            
#simple(champs)
trait_nodes(champs,traits)

'''
A,save_traits = trait_nodes(champs,traits)
B = A*A
C = B[:23,:23]
f = open('text.csv','w')
for i in range(len(C)):
    out = str(C[i])
    out = out.replace('. ',',')
    out = out.replace('.','\n')
    out = out.replace('[[','')
    out = out.replace(']]','')
    f.write(save_traits[i]+','+out)
f.close()
'''
    
