import numpy as np
import pandas as pd

#we calculate the expected outcome
#+1 means an expected outcome of 1 defender
#-1 means an expected outcome of 1 attacker



def brute(A,D,n): 
    out = 0
    if A == 0:
      return 'why would u ever put 0'
    elif D == 0:
      return 'why would u ever put 0'
      
    elif A == 1:
      for i in range(n):
          out = out + D
          defRolls = [np.random.randint(1,7) for i in range(D)]
          att = np.random.randint(1,7)
          if att > max(defRolls):
            out = out - 1
          else:
            pass
        
    elif D == 1:
      for i in range(n):
          out = out + D
          
          attRolls = [np.random.randint(1,7) for i in range(A)]
          defe = np.random.randint(1,7)
          if max(attRolls) > defe:
            out = out - 1
          else:
            pass
        
    else: # if A,D > 1  ie. (2+,2+)
    
      maxdie = min(A,D)
    
      for i in range(n):
          out = out + D

          
          defRolls = [np.random.randint(1,7) for i in range(D)]
          attRolls = [np.random.randint(1,7) for i in range(A)]
  
          defRolls = sorted(defRolls,reverse=True)
          attRolls = sorted(attRolls,reverse=True)

          defFight = defRolls[:maxdie]
          attFight = attRolls[:maxdie]
          
          for i in range(maxdie):
            if attFight[i] > defFight[i]:
              out = out - 1
            else:
              pass

              
    return out/n

maxatt = 3
maxdef = 2

data = np.zeros(shape = (maxatt*maxdef,4))

for i in range(maxatt):
  for j in range(maxdef):
    row = i*maxdef + j

    Expected= brute(i+1,j+1,1_00_000)

    data[row] = [i+1,j+1,Expected,Expected/(j+1)]
    
outdata = pd.DataFrame(data = data,
                        columns = ['NumAtt','NumDef','Expected','Expected/NumDef'],
                        index = None)
    
outdata.to_excel('outdata.xlsx')



