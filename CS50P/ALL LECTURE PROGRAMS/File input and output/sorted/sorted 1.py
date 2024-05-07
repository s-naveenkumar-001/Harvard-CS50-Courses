# creat a empty list to store values.
# using for loop we iterate each line in the file.Using append we add each values into the list.
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())
# print the values in alphabet(ascending) order.
for name in sorted(names):
    print(f"hello, {name}")
