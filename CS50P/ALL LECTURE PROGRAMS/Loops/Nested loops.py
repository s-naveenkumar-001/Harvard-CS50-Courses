# print three mario brick in column usig def keyword.

def main():
    print_column(3)
# using '\n' we print # in the column order. to deletthe extra empty line we use 'end=""'.
def print_column(height):
    print("#\n" * height, end="")
#call main function.
main()