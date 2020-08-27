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
    
def ana_data(bet,data):

    values = np.arange(1,30,0.05).tolist()
    profit_list = []
    
    tot = len(data)
    print(tot)
    win_freqs = []
    for val in values:
        profit = 0
        win_freq = 0
        for point in data:
            if val < point:
                win_freq = win_freq + 1

        win_freq = win_freq / tot
        profit = (win_freq * floor(bet*(val-1))) - (bet * (1 - win_freq))
        profit_percent = profit / bet
        
        profit_list.append(profit_percent)
        win_freqs.append(win_freq)

    
    plt.plot(values,win_freqs)
    plt.plot(values,profit_list, label = str(bet))
    plt.plot(values,[0 for i in range(len(values))],'g--')
    
    



def floor(a):
    return math.floor(a * 100)/100.0


def bet_var():
    data = get_data()
    print('Mean : '+str(sum(data)/len(data)))
    ana_data(0.01,data)
    ana_data(0.02,data)
    ana_data(0.05,data)
    ana_data(0.1,data)
    plt.legend()
    plt.show()

def split_var():
    data = get_data()
    d1 = []
    d2 = []
    d3 = []
    for i in range(len(data)):
        if i % 3 == 0:
            d1.append(data[i])
        elif i % 3 == 1:
            d2.append(data[i])
        else:
            d3.append(data[i])

    ana_data(1,d1)
    ana_data(1,d2)
    ana_data(1,d3)
    plt.show()

def hist():
    data = get_data()
    std = np.std(data)
    print(std)
    small_data = [k for k in data if k < 30]
    plt.hist(small_data,bins = 44*3,color = 'yellow',edgecolor='black')

    plt.show()


