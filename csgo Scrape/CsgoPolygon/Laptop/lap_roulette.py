import pyautogui as pag
import time
import numpy as np
import math

pag.FAILSAFE = True
pag.PAUSE = 0.5
print('Screen = '+str(pag.size()))

#COMMANDS

#pag.moveTo(X,Y,duration = (t in seconds))
#pag.moveRel(X,Y,duration = (t in seconds))
#pag.position()
#pag.click(X,Y, button = 'left')
#pag.locateOnScreen('example.png')
#pag.typewrite('Hello world!')
#pag.click(pag.center(pag.locateOnScreen('ex.png')))

#images in .png
#34 s delay?
#col = Point(x=1064, y=503)

def pos_test():
    while True:
        print(pag.position())

def run(bal):
    #time to get started
    time.sleep(10)
    red_col = (219, 121, 111)
    green_col = (125, 196, 138)
    black_col = (95, 95, 95)

    #start_bet = 5
    


    while True:

        start_bet = math.floor(bal / 2**10) # change of losing is 1/2**(num-1)
        
        while find_rolling() == False:
            pass

        print('Rolling')

        time.sleep(7)

        if pag.pixelMatchesColor(1200,545,red_col, tolerance = 10) == True:
            print('win')
            bet = start_bet
        else:
            print('loss')
            try:
                bet = bet * 2
            except:
                bet = start_bet
        
        num = abs(np.random.normal())
        
        time.sleep(9 - num)

        place_bet(bet,'red')


def place_bet(val,col):

    print('Betting: '+str(val)+' on '+col)

    pag.click(pag.center(pag.locateOnScreen('clear.png')))
    pag.moveRel(-350,0,duration = 1)
    pag.click(pag.position())
    pag.typewrite(str(val))

    pag.click(pag.center(pag.locateOnScreen(col+'.png')))

def find_rolling():

    try:
        if pag.locateOnScreen('lap_rolling.png') == None:
            print('no')
            return False
        else:

            print('found roll')
            return True
    except:
        print('NO')
        return False



    
