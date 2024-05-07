# find which student belong to which house usin match method.
# Ask input from user and print the student house.
# match function check the user input to the case.  
name =input("what's your name? ").capitalize()
match name:
    case "Harry" | "Hermoine":
        print("Griffinder")
    case "Ron":
        print("Grinffinder")
    case "Drago":
       print("slytherine")
# we use '_' underscore if user enter the unknown name it will print as 'who?'
    case _:
        print("who?")