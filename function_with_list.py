def students(names):
    print("Student Names:")
    for name in names:
        print(name)

def get_student_names():
    """
    Prompts the user to enter student names one by one.
    Returns a list of entered names.
    """

    names = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input(f"Enter student name {i+1}: ")
        names.append(name)

    return names

# Call the get_student_names function to collect user input
user_names = get_student_names()

# Call the students function with the collected names
students(user_names)
