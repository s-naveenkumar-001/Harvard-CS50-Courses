# create a main function and get input from user. using pyramid function print the mario brick.
def main():
    height = int(input("Height: "))
    pyramid(height)

# create a pyramid function and using for loop we print the range of the mario brick.
def pyramid(n):
    for i in range(n):
        print("#" * (i+1))

# To call the main function.
main()
