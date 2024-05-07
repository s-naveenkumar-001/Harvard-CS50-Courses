# creat a empty list to store the values.
names = []

# get three input from user and add that input values into the empty list.
for _ in range(3):
    names.append(input("What's your name? "))

# we print the value in the alphabetical order using 'sorted'.
for name in sorted(names):
    print(f"hello, {name}")
