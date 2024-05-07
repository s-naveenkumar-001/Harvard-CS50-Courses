# readlines() function read the file top to bottom and return the values.
# using for we iterate the each line in the file and using rstrip() we remove (right) whitespaces line.

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,",line.rstrip())