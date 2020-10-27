import random
while True:
    chance=int(input('% Chance: '))
    if random.randint(1,100)<chance:
        print('Do it')
    else:
        print('Dont do it')
