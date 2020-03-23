import matplotlib.pyplot as plt
import numpy as np
import math

def add_data():
    while True:
        num = float(input('Number: '))
        f = open('Crash Data.txt','a')
        f.write(str(num)+'\n')
        f.close()

def show_data():
    
    data = get_data()
    plt.hist(data,density = True)
    plt.show()

def get_data():
    f = open('Crash Data.txt','r')
    data = f.readlines()
    f.close()
    data = [float(d) for d in data]

    return data
    
def ana_data(bet):

    values = np.arange(1,10,0.1).tolist()
    profit_list = []
    data = get_data()
    tot = len(data)
    win_freqs = []
    for val in values:
        profit = 0
        win_freq = 0
        for point in data:
            if val < point:
                win_freq = win_freq + 1

        win_freq = win_freq / tot
        profit = (win_freq * floor(bet*(val-1)) - bet * (1 - win_freq)) / bet
        
        profit_list.append(profit)
        win_freqs.append(win_freq)

    
    plt.plot(values,win_freqs)
    plt.plot(values,profit_list)
    plt.plot(values,[0 for i in range(len(values))],'g--')
    

def floor(a):
    return math.floor(a * 100)/100.0


def bet_var():
    for i in range(10):
        ana_data((i+1) * 0.01)
    plt.show()
