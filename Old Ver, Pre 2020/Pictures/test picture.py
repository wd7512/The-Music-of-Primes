from PIL import Image
import matplotlib.pyplot as plt
file='anta2.jpg'
img=Image.open(file)
width, height = img.size
data=img.getdata()
red=[]
blue=[]
green=[]
grey=[]
redfreq=[]
greenfreq=[]
bluefreq=[]
for i in range(256):
    redfreq.append(0)
    greenfreq.append(0)
    bluefreq.append(0)
if file[-4:]=='.png':
    for (r,g,b,a) in data:
        red.append(r)
        green.append(g)
        blue.append(b)
        grey.append(r+g+b)
        redfreq[r]=redfreq[r]+1
        greenfreq[g]=greenfreq[g]+1
        bluefreq[b]=bluefreq[b]+1
if file[-4:]=='.jpg':
    for (r,g,b) in data:
        red.append(r)
        green.append(g)
        blue.append(b)
        grey.append(r+g+b)
        redfreq[r]=redfreq[r]+1
        greenfreq[g]=greenfreq[g]+1
        bluefreq[b]=bluefreq[b]+1


tot=width*height
for i in range(256):
    redfreq[i]=100*redfreq[i]/tot
    bluefreq[i]=100*bluefreq[i]/tot
    greenfreq[i]=100*greenfreq[i]/tot
redplot=[]
greenplot=[]
blueplot=[]
greyplot=[]
count=0
for i in range(height):
    redp=[]
    greenp=[]
    bluep=[]
    greyp=[]
    for j in range(width):
        redp.append(red[count])
        greenp.append(green[count])
        bluep.append(blue[count])
        greyp.append(grey[count])
        
        count=count+1
    greyplot.append(greyp)
    redplot.append(redp)
    greenplot.append(greenp)
    blueplot.append(bluep)
redx=[]
greenx=[]
bluex=[]
for i in range(width):
    rx=0
    gx=0
    bx=0
    for j in range(height):
        rx=rx+redplot[j][i]
        gx=gx+greenplot[j][i]
        bx=bx+blueplot[j][i]
    redx.append(rx/height)
    greenx.append(gx/height)
    bluex.append(bx/height)

fig,axs=plt.subplots(nrows=2,ncols=3)
ax=axs.flatten()
ax[0].imshow(greyplot,cmap='Greys_r')
ax[1].imshow(redplot,cmap='Reds')
ax[2].imshow(greenplot,cmap='Greens')
ax[4].imshow(blueplot,cmap='Blues')
ax[3].plot(redx,'r')
ax[3].plot(bluex,'b')
ax[3].plot(greenx,'g')
ax[5].plot(redfreq,'r')
ax[5].plot(bluefreq,'b')
ax[5].plot(greenfreq,'g')
plt.show()
