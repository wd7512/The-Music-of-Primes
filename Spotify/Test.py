import pyautogui as pag
'''
Spotify Full Screen

'''
xsize=pag.size()[0]
ysize=pag.size()[1]
print(pag.size())



xskip=1021
yskip=962

xsong=15
for i in range(10):

    greentick=pag.locateOnScreen('Green Tick.png', minSearchTime=5)


    ysong=greentick[1]
    songwidth=greentick[0]-xsong
    songheight=greentick[3]
    
    pag.moveTo(xskip,yskip,1)
    pag.click()
    pag.screenshot('Test'+str(i+1)+'.png',region=(xsong,ysong,songwidth,songheight))
