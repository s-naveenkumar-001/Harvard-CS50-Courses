# create a empty dictionary to store the keys and values.
grocery = {}
# To prompt the user we use while loop.
while True:
# we get input from the user.If item in grocery we add one. 
    try:
        item = input().lower()
        if item in grocery:
            grocery[item] += 1
# else we add item as a key and value as one
        else:
            grocery[item] = 1
# if user enter control + d we catch the eof error.
    except EOFError:
# print the grocery item how many times entered.
# using sorted function print all items in aphabetical order
        for key in sorted(grocery.keys()):
# print the grocery item list in all upper case
            print(grocery[key], key.upper())
# using break get out of loop
        break