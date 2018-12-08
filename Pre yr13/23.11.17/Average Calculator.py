print("This will calculate the averages of a list of numbers you input\nwhen you add a number press enter untill you are finished with your list\nthen just press enter on an empty input")
a='dfgh'
b=[]
while len(str(a))>0:
    a=input(">")
    if len(str(a)) == 0:
        end=input((sum(b))/(len(b)))
    b.append(int(a))

