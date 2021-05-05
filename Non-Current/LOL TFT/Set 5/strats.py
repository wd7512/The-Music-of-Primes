import pandas as pd

Champs = pd.read_csv('Champs.csv')
Traits = pd.read_csv('Traits.csv')
Comps = pd.read_csv('Comps.csv',header=None)



def get_traits(comp):
    all_traits = []
    for champ in comp:
        champ_stats = Champs.loc[Champs['Name'] == champ]

        print(champ_stats)

        all_traits.append(champ_stats['Traits1'])
        all_traits.append(champ_stats['Traits2'])
        all_traits.append(champ_stats['Traits3'])

    print(all_traits)





i = 0
while i != -1:
    try:
        comp = Comps.iloc[i]
        print('\nComp: ',i)
        get_traits(comp)
        i = i + 1
    except:
        i = -1