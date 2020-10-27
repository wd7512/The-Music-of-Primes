import random
import matplotlib.pyplot as plt
print('3-way rock paper scissors')
num=int(input('How many rounds do you want to play?'))
x=[0]
player1=[0]
player2=[0]
player3=[0]
move1=''
move2=''
move3=''
options=['rock','paper','scissors']

def win(var1,var2):
    if var1==var2:
        return 0
    if var1=='rock':
        if var2=='paper':
            return -1
        return 1
    if var1=='paper':
        if var2=='scissors':
            return -1
        return 1
    if var1=='scissors':
        if var2=='rock':
            return -1
        return 1
for i in range(num):
    x.append(i+1)

    
    move1=random.choice(options)
    move2=random.choice(options)
    move3=random.choice(options)

    #if max(player1)>max(player2):
        #player1=='rock'
    
    score1=win(move1,move2)+win(move1,move3)
    score2=win(move2,move1)+win(move2,move3)
    score3=win(move3,move1)+win(move3,move2)

    player1.append(player1[i]+score1)
    player2.append(player2[i]+score2)
    player3.append(player3[i]+score3)

    #print('player1 - '+move1)
    #print('player2 - '+move2)
    #print('player3 - '+move3+'\n')
    #print(player1)
    #print(player2)
    #print(player3)
    
        
plt.plot(x,player1, label='player1')
plt.plot(x,player2, label='player2')
plt.plot(x,player3, label='player3')
plt.legend()
#plt.axis('equal')
plt.show()
