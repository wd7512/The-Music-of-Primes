from PIL import Image
import matplotlib.pyplot as plt
file='scar.jpg'
img=Image.open(file)
width, height = img.size
data=img.getdata()
red=[]
blue=[]
green=[]
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
        redfreq[r]=redfreq[r]+1
        greenfreq[g]=greenfreq[g]+1
        bluefreq[b]=bluefreq[b]+1
if file[-4:]=='.jpg':
    for (r,g,b) in data:
        red.append(r)
        green.append(g)
        blue.append(b)
        redfreq[r]=redfreq[r]+1
        greenfreq[g]=greenfreq[g]+1
        bluefreq[b]=bluefreq[b]+1
tot=width*height
for i in range(256):
    redfreq[i]=red[i]/tot
    bluefreq[i]=bluefreq[i]/tot
    greenfreq[i]=greenfreq[i]/tot
redplot=[]
greenplot=[]
blueplot=[]
count=0
for i in range(height):
    redp=[]
    greenp=[]
    bluep=[]
    for j in range(width):
        redp.append(red[count])
        greenp.append(green[count])
        bluep.append(blue[count])
        
        count=count+1
    redplot.append(redp)
    greenplot.append(greenp)
    blueplot.append(bluep)



fig,axs=plt.subplots(nrows=2,ncols=2)
ax=axs.flatten()
ax[1].imshow(greenplot,cmap='Greens')
ax[2].imshow(blueplot,cmap='Blues')
ax[3].plot(redfreq,'r')
ax[3].plot(bluefreq,'b')
ax[3].plot(greenfreq,'g')
plt.show()
