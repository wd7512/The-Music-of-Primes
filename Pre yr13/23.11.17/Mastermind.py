from random import *
length=input("Choose lenth of number")
if int(length)>0:
    length=(10**(int(length))-1)
    num=randint(1, (int(length)))
    a=0
    guess='0'
    while int(num) != int(guess):
        num=list(str(num))
        guess=input((str(a)+">"))
        a=a+1
        guess=list(guess)
        guess=str(''.join(guess))
        num=str(''.join(num))
        if len(guess) != len(num):
            end=input("Wrong number of integers inputted, \npress enter to end")
            quit()
        else:
            b=''
            c=0
            for i in guess:
                if i == num[c:(c+1)]:
                    b=(b+'*')
                c=c+1
        print(b)
    print("Well done!\nyou guessed a "+str(len(num))+" letter\nlong number in "+str(a)+" guesses")
else:
    end=input("Invalid input, press enter to end")
    quit()

