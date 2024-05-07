import csv

students = []
# read the dictionary value usin csvdictreader
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
# print student name(alphabetical order) and their houses.
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")