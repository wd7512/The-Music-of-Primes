import matplotlib.pyplot as plt
from datetime import date


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

def plot(data):

    case_names = data[0]
    data_times = data[1]
    Listings = data[2]
    Medians = data[3]
    Volumes = data[4]
    Total_Val_Sold = [] #Medians * Volumes

    for i in range(len(Medians)):
        M_line = Medians[i]
        V_line = Volumes[i]

        line = []
        for i in range(len(M_line)):
            line.append(float(M_line[i]) * float(V_line[i]))

        Total_Val_Sold.append(line)

    
    fig, axs = plt.subplots(2,2)

    x_axis = [x_time_conv(d[0],d[1]) for d in data_times]

    show_names = ['Shattered-Web-Case','Glove-Case','Operation-Breakout-Weapon-Case']
    
    #show_names = case_names[:]
    print(show_names)
    
    sub_plot(axs[0,0],x_axis,Listings,'Total Listings',show_names,case_names)
    sub_plot(axs[0,1],x_axis,Medians,'Median Sale Price in last 24hr',show_names,case_names)
    sub_plot(axs[1,0],x_axis,Volumes,'Volume Sold in last 24hr',show_names,case_names)
    sub_plot(axs[1,1],x_axis,Total_Val_Sold,'Total Value Sold in last 24hr',show_names,case_names)


    plt.show()

    

def sub_plot(ax,x_axis,y_data,title,show_names,case_names):

    y_axis = []
    for line in y_data:
        new_line = [float(k) for k in line]
        y_axis.append(new_line)

    for i in range(len(show_names)):

        
        name = show_names[i]
        y = y_axis[case_names.index(name)]
        ax.plot(x_axis,y,label = name)
    ax.set_title(title)
    
    ax.legend(prop={'size': 6})

    
def x_time_conv(dat,tim):

    date_split = [int(k) for k in dat.split('/')]
    time_split = [int(k) for k in tim.split(':')]

    d0 = date(2020,3,16)
    d1 = date(date_split[2],date_split[1],date_split[0])
    date_num = (d1 - d0).days # in days

    time_num = (time_split[0]*60 + time_split[1]) # in minutes

    output_num = time_num/(24*60) + date_num # in days

    return output_num

    

data = open_files()
ana_data = analysis(data)
plot(ana_data)
