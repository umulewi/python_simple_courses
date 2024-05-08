studmarks={
    1:{'name':'alex','gender':'male','age':21},
    2:{'name':'ange','gender':'female','age':24},
    3:{'name':'james','gender':'male','age':25},
    
}

def average(a):
    sum=0
    for i in a:
        sum=a[i]['age']+sum
    # print(sum)
    averagee=sum/len(a)
    print("the average of",a[1]['age'],",",a[2]['age'],"and",a[3]['age'],"is",int(averagee))


def under(s):
    x=int(input("enter an age: "))
    for i in s:
        if(s[i]['age']<x):
            print("==============\n")
            for j in s[i]:
                print(j,":",s[i][j])


def search(s):
    name=input("enter a name: ")
    for i in s:
        if(name==s[i]['name']):
            print(s[i])
            for j in s[i]:
                print(j,":",s[i][j])