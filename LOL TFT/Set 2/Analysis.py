import itertools
from progressbar import ProgressBar
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

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
    
def clean(num):
    return round(num,10)

def save_csv(data2d,name):
    f = open(name+'.csv','w')
    for data in data2d:
        strdata = [str(a) for a in data]
        f.write(','.join(strdata)+'\n')
    f.close()


def intflt(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            try:
                array[i][j] = int(array[i][j])
            except ValueError:
                try:
                    array[i][j] = float(array[i][j])
                except ValueError:
                    pass
    return array

def main(level_size,maxcost):
    pbar = ProgressBar()
    
    champs = intflt(csv_conv('Champs.csv')[1:])
    syng = intflt(csv_conv('Traits.csv')[1:])
    
            
    low_champs = [x for x in champs if x[1] <= maxcost] #champs below maxcost
    #for a in low_champs:
        #print(a)

    size = len(low_champs)
    print(str(size)+' champions')
    total = ncr(size,level_size)
    print(str(total)+' combinations')
    low_champs_names = [x[0] for x in low_champs]
    print('Calculating Possible Combinations')
    '''
    low_champs_trips = []
    
    for a in low_champs:
        for b in low_champs:
            for c in low_champs:
                if a!=b and b!=c and c!=a:
                    low_champs_trips.append({a[0],b[0],c[0]})
    '''

    low_champs_trips = pbar(list(itertools.combinations(low_champs_names, level_size)))

    
    low_champs_trips = remove_dup(low_champs_trips)

    print(str(len(low_champs_trips))+' true sets')
    #for a in low_champs_names:
        #print(a)

    raw_chemistry = []
    eff_chemistry = []

    print('Evaluating Combinations')
    pbar = ProgressBar()
    for group in pbar(low_champs_trips):
        traits = []
        for champ in group:
            indv_trait = low_champs[low_champs_names.index(champ)][3:]
            #print(indv_trait)
            for a in indv_trait:
                if a!='':
                    traits.append(a)
        #print(traits)
        raw_chemistry.append(traits)
        
        eff_traits = []
        rec_traits = []
        for a in traits:
            if a not in rec_traits:
                rec_traits.append(a)
                eff_traits.append([a,1])
            else:
                for i in range(len(rec_traits)):
                    if a == eff_traits[i][0]:
                        eff_traits[i][1] = eff_traits[i][1] + 1

        

        count = 0
        for b in eff_traits:
            trait = b[0]
            num = b[1]
            for sy in syng:
                if sy[0] == trait and num >= sy[1]:
                    count = count + 1

        eff_traits = [count] + [list(group)] + eff_traits

        #print(eff_traits)
        eff_chemistry.append(eff_traits)

            
    '''
    for a in sorted(eff_chemistry,reverse=True):
        print(a)
    '''
    return eff_chemistry
    
def remove_dup(badlist):
    qi = set(['Qiyana_M','Qiyana_O','Qiyana_C','Qiyana_I'])

    goodlist = []
    for item in badlist:
        if item not in goodlist:
            if type(item) == tuple and len(qi.intersection(item)) > 1:
                #print('&&&&')
                pass
            else:
                goodlist.append(item)

    return goodlist
    
    
    

#a = csv_conv('Traits.csv')
#b = csv_conv('Champs.csv')

#.write(str(','.join(example)))

people = 4
maxcost = 3

data = main(people,maxcost)
save_csv(data,str(people)+'-'+str(maxcost))

end = input(':')
