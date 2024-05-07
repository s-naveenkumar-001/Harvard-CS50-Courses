# create main function in the main function call getnumber and meow functions.


def main():
    number = getnumber()
    meow(number)
# if user enter greaterthan zero using return we return the value and get out of loop.
def getnumber():
    while True:
        x = int(input("what's x? "))
        if x > 0:
            return x
# we print meow based on the user input.
def meow(n):
    for _ in range(n):
        print("meow")
# call main function.   
main()