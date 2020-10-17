'''
Have a population N that lives in X houses
Let there be Y buildings that people work at


Chance of infection depends on number of people in room and time spent

People can have 3 states. Normal, Infected, Recovered
Denoted by 0 1 2
Infected time is given by time in days T

Houses are numbered from 0 - N they stay at home
Work defines where the user goes to work
Hobby defines where the user goes the rest of the day this hobby changes every day

So the user comes into contact with 3 groups every day

Need to find a P value of being infected in the same room

'''
import numpy as np
#Infection chance
P = 0.1
#Population
N = 100
#Households
X = 30
#Workplaces
Y = 20
#Days to recover
T = 14

def random_pop(N,X,Y):
    #need [state,house,work,days since infection]
    pop = np.zeros((N,4))

    Min_House_No = np.floor(N/X)
    No_Extras = int(N/X - Min_House_No)

    pop[0] = [1,0,np.random.randint(0,Y)]
    for i in range(Min_House_No):
        pop[i+1] = [0,0,np.random.randint(0,Y)]

    return pop


a = random_pop(N,X,Y)

