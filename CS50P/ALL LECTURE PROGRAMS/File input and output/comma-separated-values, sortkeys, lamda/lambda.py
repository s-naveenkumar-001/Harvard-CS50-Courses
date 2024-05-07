# print the student names in alphabetical order.
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

# using lambda function is an anonymous function to return the student names in the student dictionary.
# using sorted function print student names in alphabetical order.
for student in sorted(students, key= lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")
