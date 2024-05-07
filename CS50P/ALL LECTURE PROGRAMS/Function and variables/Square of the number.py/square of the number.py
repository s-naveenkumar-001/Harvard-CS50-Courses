# Find a square of the number using square() function.
# create a main function and ask input from user and print the square of number using square() function.
# we use format string to print the user value in the print function.
def main():
    x = int(input("Enter the number: "))
    print(f"The square of {x} is",square(x))
# create a square function using def keyword.
# we use return function to return the value or hand over the value. 
def square(n):
# we use exponentation return n ** 2 or pow(n,2) 'pow means power of the number'. 
    return n * n
# call the main function
main()