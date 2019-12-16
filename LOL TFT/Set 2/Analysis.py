
def csv_conv(filename):
    f = open(filename,'r')
    data = f.readlines()
    f.close()
    output = []
    for line in data:
        
        newline = line.split(',')
        for i in range(len(newline)):
            if newline[i][-1:] == '\n':
                newline[i] = newline[i][:-1]
        output.append(newline)
    if len(output) == 1:
        return output[0]
    else:
        return output

def update_stats():
    champs = csv_conv('Champs.csv')
    
    

def save_csv(data,name):
    f = open(name+'.csv','w')
    strdata = [str(a) for a in data]
    f.write(','.join(strdata))
    f.close()

a = csv_conv('Traits.csv')
b = csv_conv('Champs.csv')

#.write(str(','.join(example)))

