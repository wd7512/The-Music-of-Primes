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
import math
import random
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

def random_population(N,X,Y):
    House_Pop = N/X
    Min_House_Pop = math.floor(House_Pop)
    extras = int(N * (House_Pop - Min_House_Pop))
    
    
    population = []
    infected_person = Person(1,0,random.randint(0,Y-1))
    population.append(infected_person)
    for i in range(Min_House_Pop-1):
        population.append(Person(0,0,random.randint(0,Y-1)))

    for i in range(X):
        for j in range(Min_House_Pop):
            population.append(Person(0,i+1,random.randint(0,Y-1)))

    for i in range(extras):
        population.append(Person(0,random.randint(0,X-1),random.randint(0,Y-1)))

    return population
        
class Person:
    def __init__(self,state,home,work):
        self.state = state
        self.home = home
        self.work = work
        self.time_infected = 0

def run_day(population):
    
#use matrix and numpy = much easier
