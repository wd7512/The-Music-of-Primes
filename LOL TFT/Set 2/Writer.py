#cost,origin,either,type
while True:
    name = str(input('Name:'))
    cost = str(input('Cost'))
    origin = str(input('Origin'))
    either = str(input('Either'))
    typee = str(input('Type'))
    f = open(name+'.txt','w')
    f.write(cost+','+origin+','+either+','+typee)
    f.close()
    print('\n')
