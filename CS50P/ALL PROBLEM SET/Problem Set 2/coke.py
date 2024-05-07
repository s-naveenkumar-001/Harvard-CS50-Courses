# we store a value in variable
amount_due = 50
# using while loop we loop until it become zero and print amountdue and get input fro the user
# (if user enter an unassigned value it will loop until get the assigned value)
while amount_due > 0:
    print("Amount Due: ",amount_due)
    coin =int(input("insert coin: "))
# using if and list we wheather the user enter value is there if there it will execute
    if coin in [25, 10, 5]:
        amount_due -= coin
# using abs(), function we get the absolute value and print the change owed(the remaining coin)
        amount_due = abs(amount_due)
        print("Change Owed: ",amount_due) 