students = [
    {"name" : "Hermoine", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
    {"name" : "Padma", "house" : "Ravenclaw"},
]

# we also use " list() " keyword for empty list
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)