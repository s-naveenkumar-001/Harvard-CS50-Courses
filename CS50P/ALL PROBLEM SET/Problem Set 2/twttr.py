# Get input from user and print the output.
answer = input("Input: ")
print("Output: ", end="")
# its remove the specific letter and print remaining and its help to manage the time and space.
for letter in answer:
    if not letter in ["a", "e", "i", "o", "u"]:
        print(letter, end="")
print()