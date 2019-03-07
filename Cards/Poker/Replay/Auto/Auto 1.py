import pyautogui as pag
import time
print('Please put the cursor on the top left corner\nof your cards for the next 5 seconds')
for i in range(5):
    print(5-i)
    time.sleep(1)
cali=pag.position()
print('Calibrated to\nx='+str(cali[0])+'\ny='+str(cali[1]))
