import cv2
import numpy as np

def blank(x,y): #640 480
    
    row = []
    for a in range(x):
        row.append([1,1,1])
    tot=[]
    for a in range(y):
        tot.append(row)

    return np.array(tot)

def blend(f):
    y, x, null = f.shape

    mat = blank(x,y)
    
    mat[0] = f[0]
    mat[y-1]= f[y-1]

    

    for a in range(x-2):
        for b in range(y-2):
            v1 = f[b][a]
            v2 = f[b][a+1]
            v3 = f[b][a+2]
            v4 = f[b+1][a+2]
            v5 = f[b+2][a+2]
            v6 = f[b+2][a+1]
            v7 = f[b+2][a]
            v8 = f[b+1][a]
            
            u = v1+v2+v3+v4+v5+v6+v7+v8
            
            u[0] = round(u[0]/8)
            u[1] = round(u[1]/8)
            u[2] = round(u[2]/8)
            
            mat[b+1][a+1] = u
                

    return mat
    
    

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    print('f')
    cv2.imshow("preview", blend(frame))
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
