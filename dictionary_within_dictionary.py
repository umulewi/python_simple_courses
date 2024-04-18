S={ 1:{"name":"jack","age":20,"reg_no":"21rp01283"},
    2:{"name":"mucyo","age":100,"reg_no":"21rp899"},
    3:{"name":"alex","age":90,"reg_no":"21rp4899"}}
 
# print(S[1])
# print(S[1]["name"])
# print(S[2]["age"])

#print key with value

# for j  in S:
#     i = S[j]
#     print(j, ":",i)


#print 3 names using loop

# for x in S:
    
#     print(S[x]['name'])


#average age

sum=(S[1]["age"])+(S[2]["age"])+(S[3]["age"])
average=sum/3
print (average)

#using loop
y=0
count =0
for x in S:
    age= int(S[x]["age"])
    y=y+age
    count=count+1
print(float(y/count))

#marks



marks = {
    "jack": {"ICT": 66, "MATH": 77, "physics": 88},
    "alex": {"ICT": 66, "MATH": 77, "physics": 88},
    "paul": {"ICT": 66, "MATH": 77, "physics": 88}
}

average_marks = {}

for student, subjects in marks.items():
    total_marks = sum(subjects.values())
    num_subjects = len(subjects)
    average_marks[student] = total_marks / num_subjects

print("Average marks:")
for student, average_mark in average_marks.items():
    print(student, ":", average_mark)

#return minimum

# if S[1]["age"]>S[2]["age"]:
#     print(S[1]["age"])
   
# elif S[2]["age"]>S[3]["age"]:
#     print(S[2]["age"])
# elif S[3]["age"]>S[1]["age"]:
#     print(S[3]["age"])
# else:
#     print("all numbers are equaal")

#using loop
S = {
    1: {"name": "jack", "age": 20, "reg_no": "21rp01283"},
    2: {"name": "mucyo", "age": 100, "reg_no": "21rp899"},
    3: {"name": "alex", "age": 100, "reg_no": "21rp4899"}
}
# max_age = float('-inf')  

for key in S:
    if S[key]["age"] > max_age:
        max_age = S[key]["age"]

print("Maximum age:", max_age)






