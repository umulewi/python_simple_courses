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

average(studmarks)        
        

