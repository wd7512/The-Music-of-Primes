
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

a = csv_conv('Traits.csv')
b = csv_conv('Champs.csv')
