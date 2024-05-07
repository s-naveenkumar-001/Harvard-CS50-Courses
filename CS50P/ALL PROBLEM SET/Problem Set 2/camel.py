# Get input from user
camelCase =input("camelCase: ")
print("snake_case: ",end="")
# print a snake case:
for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter,end="")

print()
