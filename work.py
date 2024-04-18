marks = {
    "jack": {"ICT": 66, "MATH": 77, "physics": 88},
    "alex": {"ICT": 56, "MATH": 67, "physics": 68},
    "paul": {"ICT": 60, "MATH": 70, "physics": 80}
}

average = {}
for student, courses in marks.items():
    total_marks = sum(courses.values())
    num_courses = len(courses)
    average[student] = total_marks / num_courses

print("AVERAGE MARKS:")
for student, average_mark in average.items():
    print(student, ":", average_mark)