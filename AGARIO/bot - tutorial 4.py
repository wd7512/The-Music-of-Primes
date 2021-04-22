import cv2 as cv
import pyautogui as pag
import numpy as np
from time import time
from PIL import ImageGrab
from vision import findClickPositions

mid_x = 1920/2
mid_y = 1080/2
loop_time = time()
while True:
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot,cv.COLOR_RGB2GRAY)
    
    #cv.imshow('Computer Vision',screenshot)

    pag.moveTo(mid_x,mid_y)
    foods = findClickPositions('food.png',screenshot,0.8)

    

    if len(foods):
        closest = foods[0]
        for loc in foods:
            if abs(mid_x - loc[0]) + abs(mid_y - loc[1]) < abs(mid_x - closest[0]) + abs(mid_y - closest[1]):
                closest = loc

        pag.moveTo(closest[0],closest[1])

        
    
    print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows
        break

print('Done.')
