students = [
    {"name" : "Hermoine", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

griffindors = filter(is_gryffindor, students)

for gryffindor in sorted(griffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])