# we create 'names.txt' file.
name = input("Wat's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
