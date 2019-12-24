from progressbar import ProgressBar
pbar = ProgressBar()

filename = '5-3.csv'

f = open(filename,'r')
print('reading file')
data = pbar(f.readlines())
f.close()
comp = []
print('compressing data')
for lines in data:
    comp.append((((lines.replace(']','')).replace('[','')).replace("'",'')).replace('"',''))

f = open('comp '+filename,'w')
pbar = ProgressBar()
print('saving data')
for a in pbar(comp):
    #print(comp)
    f.write(a)
f.close()
