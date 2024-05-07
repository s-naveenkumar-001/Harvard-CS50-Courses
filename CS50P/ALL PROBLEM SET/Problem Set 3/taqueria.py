# taqueria menu list
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# we create a variable to store the values
total_amount = 0
# using while loop prompt the user until user enter (contrl + d)
while True:
    try:
        item = input("Item: ").title()
# if user enter item in menu add the item value in the total_amount
        if item in menu:
            total_amount += menu[item]
# print the total amount and using format string round the value
# using end="" print two the two values same line
            print("Total: $", end="")
            print(f"{total_amount:.2f}")
# if user inputs control + d catch the EOF error and print empty line
# using break get out of the loop 
    except EOFError:
        print()
        break