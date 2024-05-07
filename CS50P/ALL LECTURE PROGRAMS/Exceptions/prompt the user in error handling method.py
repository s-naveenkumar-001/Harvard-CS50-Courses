# In this program we prompt the user until we get input as integer.
# we also write the message inside of our own function.

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()