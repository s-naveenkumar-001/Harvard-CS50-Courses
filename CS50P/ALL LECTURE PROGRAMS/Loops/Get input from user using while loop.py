# print moew based on user input using while loop.
# if user enter greater than zero using break it get out of the loop and print meow based on the user input else while true it continue the loop.
# we use break to get out of the loop.
while True:
    n = int(input("what's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")