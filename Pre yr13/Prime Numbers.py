def partb(num, count):
    while 1==1:
        check=0
        count=num=num+1
        while count>2:
            count=count-1
            test=num%count
            if test==0:
                partb(num, count)
        end=input(str(num)+" is prime")
    
opt=input("Do you want to test if a number is prime or[a]\nlist prime numbers[b]")
if opt=='a':
    num=count=int(input("Number:"))
    if num >= 1:
        end=input(num+' is not prime')
        quit()
    while count>2:
        count=count-1
        test=num%count
        if test==0:
            end=input(str(num)+" is not prime\nit is divisible by "+str(count))
            quit()
    end=input(str(num)+" is prime")
    quit()
elif opt=='b':
    num=count=1
    partb(num, count)
