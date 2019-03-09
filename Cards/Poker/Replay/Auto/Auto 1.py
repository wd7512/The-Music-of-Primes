import pyautogui as pag
import time


timer=5
print('Please put the cursor on the top left corner\nof your cards for the next '+str(timer)+' seconds')
for i in range(timer):
    print(timer-i)
    time.sleep(1)
cali=pag.position()
print('Calibrated to\nx='+str(cali[0])+'\ny='+str(cali[1]))

def getpot():
    pot=[570,530]
    potsize=[70,30]#width height
    pag.screenshot('pot.png',pot+potsize)

def getstack(cali):
    stack=[cali[0]+20,cali[1]+113]
    stacksize=[100,30]
    pag.screenshot('stack.png',stack+stacksize)

    

getpot()
getstack(cali)
