# find te given student is belong to which house.
# we use condition to find the student house. we ask input from user and we use capitalize function to change the given words first letter to uppercase.
name = input("what's your name? ").capitalize()
# we logical "or" it will check both case if any one is true it will print the house.
if name == "Harry" or name == "Hermoine":
    print("Griffinder")
elif name == "Ron":
    print("Griffinder")
elif name == "Drago":
    print("slytherine")
else:
    print("who?")