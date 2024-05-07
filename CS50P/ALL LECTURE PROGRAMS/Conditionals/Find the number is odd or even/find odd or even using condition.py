# Ask input from user and find the given input is add or even using condition.
x =int(input("Enter the number: "))
# we use modulo the given number remainder is equal to zero it is even else it is odd.
if x%2==0:
    print("The given number is even")
else:
    print("The given number is odd")