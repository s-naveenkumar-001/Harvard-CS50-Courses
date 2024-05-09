# create a mario brick using hashtag "#" first line one brick and second line two brick and third line three brick.
# likewise create a mario brick and any error acquires debug it. 

# create a main function and get input from user. using pyramid function print the mario brick.
def main():
    height = int(input("Height: "))
    pyramid(height)

# create a pyramid function and using for loop we print the range of the mario brick.
def pyramid(n):
    for i in range(n):
        # This line start from zero. so if we multifly it the first line will be zero brick.
        # using debug we find the error and fix it. if we add one to the variable "i". 
        # It will print the mario brick.
        # print("#" * i)
        print("#" * (i+1))

# To call the main function.
main()