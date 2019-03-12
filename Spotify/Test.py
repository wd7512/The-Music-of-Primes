import pyautogui as pag
'''
Spotify Full Screen

'''
xsize=pag.size()[0]
ysize=pag.size()[1]
print(pag.size())



xsong=182
ysong=170
songheight=40
songwidth=320


#while True:
    #print(pag.position())
for i in range(10000):
    
    greentick=pag.locateCenterOnScreen('Next.png', minSearchTime=10)


    
    
    
    pag.screenshot('Test'+str(i+1)+'.png',region=(xsong,ysong,songwidth,songheight))

    pag.moveTo(greentick[0],greentick[1])
    pag.click()
    pag.moveTo(greentick[0]+50,greentick[1])
