import matplotlib.pyplot as plt


def open_files():
    files = ['Listings.csv',
             'Medians.csv',
             'Volumes.csv']

    data = []
    
    for file in files:
        f = open(file,'r')
        data.append([(k.replace('\n','')).split(',') for k in f.readlines()])

    Key = data[0][0]

    Listings = data[0][1:]
    Medians = data[1][1:]
    Volumes = data[2][1:]
    

    return [Key,Listings,Medians,Volumes]

def analysis(data):
    case_names = data[0][2:]
    data_times = [k[:2] for k in data[1]]

    
    Case_Listings = [[k] for k in data[1][0][2:]]
    Case_Medians = [[k] for k in data[2][0][2:]]
    Case_Volumes = [[k] for k in data[3][0][2:]]

    for i in range(len(data[1]) - 1):
        for j in range(len(data[1][0]) - 2):
            Case_Listings[j].append(data[1][i+1][j+2])
            Case_Medians[j].append(data[2][i+1][j+2])
            Case_Volumes[j].append(data[3][i+1][j+2])

    return [case_names,data_times,Case_Listings,Case_Medians,Case_Volumes]

def plot(case_names,data_times,values):

    x_axis = [str(k) for k in data_times]
    y_axis = []
    for line in values:
        new_line = [float(k) for k in line]
        y_axis.append(new_line)

    for i in range(len(case_names)):

        y = y_axis[i]
        name = case_names[i]
        plt.plot(x_axis,y,label = name)

    plt.xticks(rotation=90)
    plt.legend()
    plt.show()
    

data = open_files()
ana_data = analysis(data)
plot(ana_data[0],ana_data[1],ana_data[4])
