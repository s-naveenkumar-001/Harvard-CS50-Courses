# using while loop we get input as integer from user if user enter string we give instruction to enter the integer value.
# if user enter integer try using break get out of the loop and execute the print function. 
while True:
    try:
        x = int(input("what's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"{x} is an integer")