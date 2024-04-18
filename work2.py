marks = {
    "jack": {"ICT": 170, "MATH": 77, "physics": 88},
    "alex": {"ICT": 66, "MATH": 77, "physics": 88},
    "paul": {"ICT": 66, "MATH": 77, "physics": 88}
}

average_marks = {}
for student, courses in marks.items():
    total_marks = 0
    i = 0
    for courses, mark in courses.items():
        total_marks =total_marks+ mark
        i += 1
    average_marks[student] = total_marks / i
print("THE AVERAGE MARKS ARE:")
for student, average_mark in average_marks.items():
    print(student, ":", average_mark)
