# we try something in try function if something goes wrong. the except function will catch the error.
# if no error occurs the else statement will executed.
try:
    x = int(input("whats x? "))
except ValueError:
    print(f"x is not an integer")
else:
    print(f"{x} is an integer")
