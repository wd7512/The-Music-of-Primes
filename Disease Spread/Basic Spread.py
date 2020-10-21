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
import matplotlib.pyplot as plt


#Infection chance
P = 0.1
#Population
N = 1_00_000
#Households
#avg household size in uk is 2.3
X = int(N/2.3)
#Workplaces or use as day contacts
#where avg. number of contacts a day is N/Y
Y = int(N/10)
#Days to recover
T = 14

def random_pop(N,X,Y):
    #need [state,house,work,days since infection]
    pop = np.zeros((N,4),dtype = int)

    Min_House_No = int(np.floor(N/X))
    No_Extras = int(N - Min_House_No*X)

    n = 0
    pop[n] = [1,0,np.random.randint(0,Y),0]
    n = n+1
    for i in range(Min_House_No-1):
        pop[n] = [0,0,np.random.randint(0,Y),0]
        n = n+1

    for i in range(X-1):
        for j in range(Min_House_No):
            pop[n] = [0,i+1,np.random.randint(0,Y),0]
            n = n+1


    for i in range(No_Extras):
        pop[n] = [0,np.random.randint(0,X),np.random.randint(0,Y),0]
        n = n+1


    return pop

def run_day(Population,P,T):

    infected = np.where(Population[:,0] == 1)[0] #gets infected indexes
    chance = int(1/P)

    for i in infected:
        infected_person = Population[i]
        
        house = infected_person[1] #house with infected person
        housemates = np.where(Population[:,1] == house)[0]

        for j in housemates:
            person = Population[j] #housemate
            if person[0] == 0: #if not infected
                if np.random.randint(0,chance) == 0: #chance to be infected
                    person[0] = 1 #now infected        
        
        work = infected_person[2]
        workmates = np.where(Population[:,2] == work)[0]

        for j in workmates:
            person = Population[j]
            if person[0] == 0: #if not infected
                if np.random.randint(0,chance) == 0: #chance to be infected
                    person[0] = 1 #now infected

        if infected_person[3] > T: #if infected for 14 days
            infected_person[0] = 2 #become non-infectious

        infected_person[3] = infected_person[3] + 1 #add day to infected

    return Population
            
def run_to_end(Population,P,T):

    day = 0
    uninfected = [np.sum(Population[:,0] == 0)]
    infected = [np.sum(Population[:,0] == 1)]
    recovered = [np.sum(Population[:,0] == 2)]


    while infected[-1] != 0: #while there exists someone infected

        print('Day: '+str(day)+' Inf: '+str(infected[-1]))

        day = day + 1
        
        Population = run_day(Population,P,T)

        uninfected.append(np.sum(Population[:,0] == 0))
        infected.append(np.sum(Population[:,0] == 1))
        recovered.append(np.sum(Population[:,0] == 2))



    return uninfected,infected,recovered
        



uninf,inf,rec = run_to_end(random_pop(N,X,Y),P,T)

x = list(range(0,len(uninf)))
y = np.zeros((len(uninf))) + N
plt.plot(x,y)
plt.stackplot(x,inf,rec)



plt.show()



