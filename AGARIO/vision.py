import cv2 as cv
import pyautogui as pag
import time
import numpy as np

def findClickPositions(needle_img_path, haystack_img, threshold = 0.5, debug_mode = None):

    needle_img = cv.imread(needle_img_path,cv.IMREAD_GRAYSCALE)

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]


    result = cv.matchTemplate(haystack_img,needle_img,cv.TM_CCOEFF_NORMED)
    #cv.imshow('Result',result)

    locations = np.where(result >= threshold)

    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]),int(loc[1]),needle_w,needle_h]
        rectangles.append(rect)
        #can repeat line above as grouping removes single rects

    rectangles,weights = cv.groupRectangles(rectangles,1,0.1)

    #print(rectangles)
        
    points = []
    if len(rectangles):
        print('Found needle(s).')
        
        
        line_color = (0,0,0)
        line_type = cv.LINE_4

        marker_color = (0,0,0)
        marker_type = cv.MARKER_CROSS

        for (x,y,w,h) in rectangles:

            center_x = x + int(w/2)
            center_y = y + int(h/2)

            points.append((center_x,center_y))

            if debug_mode == 'points':
                cv.drawMarker(haystack_img, (center_x,center_y), marker_color, marker_type)
            elif debug_mode == 'rectangles':
                top_left = (x,y)
                bottom_right = (x + w, y + h)

                cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)


        if debug_mode:
            cv.imshow('Matches',haystack_img)


    return points

