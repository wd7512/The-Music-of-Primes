import matplotlib.pyplot as plt
import random


def run(trials):
    line=[]
    count=0

    for i in range(trials):
        count=count-1+2*random.randint(0,1)
        line.append(count)

    predict1=[0]
    predict2=[0]
    
    for i in range(trials-1):
        if abs(line[i])<4:
            predict1.append(predict1[-1])
        elif line[i]>0 and line[i+1]<line[i]:
            predict1.append(predict1[-1]+1)
        elif line[i]<0 and line[i+1]>line[i]:
            predict1.append(predict1[-1]+1)
        else:
            predict1.append(predict1[-1]-1)
    

    for i in range(trials-1):
        if line[i]>0 and line[i+1]<line[i]:
            predict2.append(predict2[-1]+1)
        elif line[i]<0 and line[i+1]>line[i]:
            predict2.append(predict2[-1]+1)
        elif line[i]==0:
            predict2.append(predict2[-1])
        else:
            predict2.append(predict2[-1]-1)


          
    subtrials=int(trials/10)

    subline=[]
    subpredict1=[]
    subpredict2=[]

    for i in range(10):
        subline.append(line[subtrials*i])
        subpredict1.append(predict1[subtrials*i])
        subpredict2.append(predict2[subtrials*i])


    plt.subplot(1,3,1)
    plt.plot(line,predict1)
    plt.plot(subline,subpredict1,'-o')
    plt.axis('Square')



    plt.subplot(1,3,2)
    plt.plot(line,predict2)
    plt.plot(subline,subpredict2,'-o')
    plt.axis('Square')

    plt.subplot(1,3,3)
    plt.plot(predict1,label='Predict1')
    plt.plot(predict2,label='Predict2')
    plt.plot(line,label='Line')
    plt.plot([0,trials],[0,0],'--')
    plt.legend()

    plt.show()
    
    return predict2[-1]

trials=int(input('Trials:'))
'''
data=0
for i in range(20):
    runs=100
    
    for i in range(runs):
        data=data+run(trials)/runs
    print(data)
'''
run(trials)
