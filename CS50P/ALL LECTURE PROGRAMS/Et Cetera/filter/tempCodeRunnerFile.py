students = [
    {"name" : "Hermoine", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
]


griffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(griffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])