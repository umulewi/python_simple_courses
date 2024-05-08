def manipulate_list():
    myList = []
    n = int(input("How many items do you want to add? "))
    for i in range(n):
        item = input("Enter item: ")
        myList.append(item)
    
    print("Original List:", myList)
    myList.sort() 
    print("Sorted List:", myList)
    return myList

result_list = manipulate_list()

