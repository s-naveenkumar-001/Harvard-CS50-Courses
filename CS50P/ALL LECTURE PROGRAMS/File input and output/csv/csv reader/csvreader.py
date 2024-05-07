# import csv module and using 'csvreader()' we separate the values for us.
import csv

students = []
# using for loop we values in dictionary keys and we add dictionary into the list.
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})
# print students name in alphabetical order using lambda function.
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
