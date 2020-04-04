def fix_file(filename):
    f = open(filename,'r')
    data = f.readlines()
    f.close()
    names = data[0][:-1]
    
    
    data = data[1:]
    new_data = []
    emp = []
    dates = []
    for i in range(len(data)):
        line = data[i]
        new_line = line.split(',')
        dates.append(new_line[:2])
        new_line = new_line[2:]
        
        if new_line[0] == ' ':
            emp.append(i)
        else:
            new_line = [float(a) for a in new_line]
        
        
        new_data.append(new_line)
        
    if len(emp) > 0:
        #print(emp)
        start_emp = new_data[emp[0]-1]
        end_emp = new_data[emp[-1]+1]
        frac = len(emp)
        diff_emp = [(end_emp[i] - start_emp[i]) / frac for i in range(len(start_emp))]

        count = 1
        for i in emp:

            new_line = [ron(start_emp[k]+(diff_emp[k]*(count))) for k in range(len(start_emp))]
            new_data[i] = new_line
            count = count + 1

    fix_data = [names]
    for i in range(len(new_data)):
        K = new_data[i]
        dat = dates[i]
        
        fix_data.append(dat+K)

    return fix_data

def ron(num):
    num = num * 100
    num = round(num)
    return num/100


filenames = ['Listings.csv',
            'Medians.csv',
            'Volumes.csv']

files = []
for file in filenames:
    a = fix_file(file)
    files.append(a)
    f = open('FIX' + file,'w')
    for line in a:
        w = str(line)
        w = w.replace(']','')
        w = w.replace('[','')
        w = w.replace("'",'')
        
        
        f.write(w + '\n')
    f.close()
        
