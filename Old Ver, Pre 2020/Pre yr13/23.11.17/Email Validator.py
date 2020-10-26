email=input("input email: ")
if len(email)==0:
    quit()
i=''
num=0
while 1==1:
    for i in email:
        if i == ' ':
            end=input('You have a space in you email\ndid you mean\n'+email.replace(' ','')+'?\n[y/n]: ').lower
            if end == 'y':
                email=email.replace(' ','')
            else:
                quit()
        elif i == '@':
            num = num + 1
            while i == '@':
                for i in email:
                    if i == ' ':
                        end=input('You have a space in you email\ndid you mean\n'+email.replace(' ','')+'\n[y/n]').lower
                        if end == 'y':
                            email=email.replace(' ','')
                        else:
                            quit()
                if email[-4:] == '.com':
                    end=input(email+' is in the correct format')
                    quit()
                else:
                    end=input('You need a .com on the end\ndid you mean\n'+email+'.com\n[y/n]')
                    if end == 'y':
                        email=(str(email)+'.com')
                    else:
                        quit()
    if num == 0:
        end=input("Your email is missing @")
        quit()

        

