# print the student name in alphabetical order.
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

# creat a function get_name to return student name in the dictionary.
def get_name(student):
    return student['name']

# using sorted function print students name alphabetically.
for student in sorted(students, key= get_name):
    print(f"{student['name']} is in {student['house']}")
