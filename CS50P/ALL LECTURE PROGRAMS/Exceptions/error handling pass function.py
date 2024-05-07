# we prompt the user until we get input as integer.
# we use "pass" in except method to say nothing. the except function catch the error but say nothing.
def main():
    x = get_int()
    print(f"x is {x}")

# using while loop we prompt the user.
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
# call main function.
main()