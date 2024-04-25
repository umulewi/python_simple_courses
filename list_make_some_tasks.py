# def students(names):
#     for x in names:
#         print (x)


# z=['lewis','danny','alice','aline','shema']

# students(z)

# def get_students():
#     students = []
#     while len(students) < 5:
#         student = input("Enter student name (press Enter to stop): ")
#         if not student:
#             break
#         students.append(student)
#     return students

# def display_students(students):
#     print("List of students:")
#     for idx, student in enumerate(students, 1):
#         print(f"{idx}. {student}")

# def main():
#     print("Enter names of students (maximum 5):")
#     students = get_students()
#     display_students(students)

# if __name__ == "__main__":
#     main()

def students():
    names = []
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        name = input(f"Enter student name {i+1}: ")
        names.append(name)

    print("\nStudent Names:")
    for name in names:
        print(name)

students()
