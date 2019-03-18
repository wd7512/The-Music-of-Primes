import time
st=input('Press Enter to Start Timer')
start=time.time()
en=input('Press Enter to End Timer')
end=time.time()
diff=round(end-start)
print('Your time is '+str(diff)+' seconds')
f=open('Best Time.txt','r')
best=f.readline()
f.close()
f=open('Best Time.txt','w')
if int(best)<diff:
    f.write(diff)
else:
    diff=int(best)
f.close()
print('Best Time is '+str(diff)+' seconds')
