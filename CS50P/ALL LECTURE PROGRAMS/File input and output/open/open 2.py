# open a file and add the input values into the file.
# Using '\n' we print empty line.
name = input("What's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
