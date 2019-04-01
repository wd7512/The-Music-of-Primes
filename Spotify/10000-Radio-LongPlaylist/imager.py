from PIL import Image
import matplotlib.pyplot as plt

for i in range(10000):
    print(i)
    file='Test'+str(1+i)+'.png'
    col=[]
    img=Image.open(file)
    width, height = img.size
    for (r,g,b) in img.getdata():
        col.append(r)
    plot=[]
    count=0
    for i in range(height):
        plotp=[]
        for j in range(width):
            plotp.append(col[count])
            count=count+1
        plot.append(plotp)
    plt.imshow(plot[6:],cmap='Greys')
    plt.show()
    #plt.savefig('TTest'+str(i+1)+'.png')
    plt.clf()
