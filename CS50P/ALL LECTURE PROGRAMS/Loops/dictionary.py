# dictiony have two type of data one key and another one value we use keys to find the values.
# in dictionary we use curvely barcket to save the data.
students = {"Harry" : "Griffinder",
        "Hermoine" : "Griffinder",
         "Ron" : "Griffinder",
         "Drago" : "slytherine",
         }
# we keys to print the specific values.
#print(students["Harry"])
# using for loop in the print function we use keys to print the values and we print the key using sep=", " we add coma in the key and value.
for student in students:
    print(student,students[student], sep=", ")