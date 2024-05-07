# create a main function
def main():
# usin loop prompt the user input and get input from user
    while True:
        fuel = input("Fraction: ")
        try:
# using split function split the user enter value into two
            x, y = fuel.split("/")
# make x and y integer using int function
            new_x = int(x)
            new_y = int(y)
# divide x and y. if "f" is less than one print fuel percentage and using break function get out of the loop
            f = new_x / new_y
            if f <= 1:
                print_fuel(f)
                break
#using except catch the value and zerodivsion error and say nothing using pass function
        except(ValueError, ZeroDivisionError):
            pass
# check the fuel level using conditions
def print_fuel(n):
    percentage = round(n * 100)
# if fuel percentage less than or equal to one print "E"
    if percentage <= 1:
        print("E")
# if fuel percentage greater than or equal to "99" print "F"
    elif percentage >= 99:
        print("F")
# print the fuel percentage
    else:
        print(f"{percentage}%")

# call main function
main()