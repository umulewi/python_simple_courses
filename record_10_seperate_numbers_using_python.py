def findmin():
    a=int(input("enter a 10 numbers"))
    max=a
    min=a
    i=2
    while i<=5:
        x=int(input("enter a number"))
        if min>a:
            min=a
        elif max<a:
            max=a
        i=i+1
    print(max)
    print(min)
findmin()
