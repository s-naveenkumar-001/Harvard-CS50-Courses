# create one file write the input into file.
name = input("What's your name? ")
# 'open' a file and write the values into the file and close the file.
file = open ("names.txt", "w")
file.write(name)
file.close()
