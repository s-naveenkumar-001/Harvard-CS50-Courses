
# get input from user
item = input("Item: ").lower()
# Using conditions check the user input 
if item == "apple":
    print("Calories: 130")
elif item == "avocado" or item == "cantaloupe" or item == "honeydew melon" or item == "nectarine":
    print("Calories: 50")
elif item == "banana":
    print("Calories: 110")
elif item == "grapefruit" or item == "kiwifruit" or item == "peach":
    print("Calories: 60")
elif item == "grapes":
    print("Calories: 90")
elif item == "lemon":
    print("Calories: 15")
elif item == "lime":
    print("Calories: 20")
elif item == "orange" or item == "watermelon":
    print("Calories: 80")
elif item == "pear" or item == "sweet cherries":
    print("Calories: 100")
elif item == "pineapple" or item == "strawberries" or item == "tangerine":
    print("Calories: 50")
elif item == "plums":
    print("Calories: 70")
# print the user input 
    print(item)