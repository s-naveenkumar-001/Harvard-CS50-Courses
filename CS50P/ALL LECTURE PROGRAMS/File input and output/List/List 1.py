# creat a empty list to store the values.
names = []
# get three input from user and add that value into the empty list using 'append()'.
for _ in range(3):
    name = input("Whats your name? ")
    names.append(name)

# print the list values
for name in names:
    print(f"hello, {name}")
