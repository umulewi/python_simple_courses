def students(names):
    print("students name are:")
    i=1
    for x in  names:
        print(i,'.',x)
        i=i+1
def get_student_name(names=[]):
   
    nbr_of_students=int(input("enter a number"))
    for i in range(nbr_of_students):
        name=input(f"enter student name {i+1}")
     
        names.append(name)
    return names

username=get_student_name()
students(username)






        
