# using for loop we print each line in the file.
# using rstrip() we remove the whitespaces.
with open("names.txt", "r") as file:
    for line in file:
        print("hello,",line.rstrip())