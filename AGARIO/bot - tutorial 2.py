import cv2 as cv
import pyautogui as pag
import time
import numpy as np

needle_img = cv.imread('food.png',cv.IMREAD_GRAYSCALE)
haystack_img = cv.imread('haystack.png',cv.IMREAD_GRAYSCALE)



result = cv.matchTemplate(haystack_img,needle_img,cv.TM_CCOEFF_NORMED)
#cv.imshow('Result',result)


threshold = 0.85
locations = np.where(result >= threshold)

locations = list(zip(*locations[::-1]))

if locations:
    print('Found needle(s).')
    
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    line_color = (0,0,0)
    line_type = cv.LINE_4

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

    cv.imshow('Matches',haystack_img)

    cv.waitKey()

else:
    print('Needle not found.')
