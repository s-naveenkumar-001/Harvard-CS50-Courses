# print the square of mario brick 3*3.
# print three column and row of brick using your own function.
def main():
    print_square(3)
# print the column of te brick and call te print _row() function.
def print_square(size):
    for i in range(size):
        print_row(size)
# print row of the mario brick using multiplication.
def print_row(n):
    print("#" * n)  
# call main function.
main()