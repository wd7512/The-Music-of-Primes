name=input("What word would you like to put in banner:")
line1=""
if (len(name)) > 0 :
    a=len(name)+4
    while a > 0:
        line1=(line1+"*")
        a=a-1
    print(line1)
    print("* "+str(name)+" *")
    print(line1)
else:
    end=input("Your word needs to be greater than one char \npress enter to end")
