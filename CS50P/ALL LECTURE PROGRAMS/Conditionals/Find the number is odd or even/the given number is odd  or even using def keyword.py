# Find the given number is odd or even using our own is_even() function.
# create a main function ask input from the user.
def main():
    x =int(input("what is x? "))
    if is_even(x):
        print("The given number is even")
    else:
        print("The given number is odd")
# we create a function called is_even(). if the given number remainder is zero it return True else its return False.
# we use boolean values True or False. 
def is_even(n):
# retrun True if n%2==0 else return as False (or) return n%2==0
    if n%2==0:
        return True
    else :
        return False
# call the main function   
main()