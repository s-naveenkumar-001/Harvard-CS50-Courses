# we create our own function to get input as an integer.
# If user enter integer in get_int() function is return the value.otherwise the except function will catch the error.
# we another method "return int(input("What's x? "))" and we remove the else because we return the value after we get it in the try function.
def main():
    x = get_int()
    print(f"{x} is an integer")

def get_int():
    try:
        n =int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        return n
# call main function.   
main()
