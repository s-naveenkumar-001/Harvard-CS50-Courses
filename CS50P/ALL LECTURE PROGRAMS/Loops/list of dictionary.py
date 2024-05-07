# list of dictionaries
# in this dictionary we create name,house and patronus as key and we give value .
# using for loop we print values in the key.
students = [{"name" : "Harry", "House" : "Griffinder", "patronus" : "otter"},
            {"name" : "Hermoine", "House" : "Griffinder", "patronus" : "stay"},
            {"name" : "Ron", "House" : "Griffinder", "patronus" : "jack russell terrire"},
            {"name" : "Drago", "House" : "slytherine", "patronus" : None},
           ]

for student in students:
    print(student["name"],student["House"],student["patronus"], sep=", ")