import cv2 as cv
import pyautogui as pag
import time
import numpy as np

needle_img = cv.imread('player.png',cv.IMREAD_GRAYSCALE)
haystack_img = cv.imread('haystack.png',cv.IMREAD_GRAYSCALE)

#cv.imshow('needle',needle_img)
#cv.imshow('haystack',haystack_img)

result = cv.matchTemplate(haystack_img,needle_img,cv.TM_CCOEFF_NORMED)

#cv.imshow('Result',result)
#cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

threshold = 0.8
if max_val >= threshold:
    print('Found needle')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    
    cv.rectangle(haystack_img, top_left, bottom_right,
                 color=(0,255,0), thickness=2,lineType=cv.LINE_4)

    #cv.imshow('Result',haystack_img)
    #cv.waitKey()

    cv.imwrite('result.jpg',haystack_img)
else:
    print('Needle not found.')
