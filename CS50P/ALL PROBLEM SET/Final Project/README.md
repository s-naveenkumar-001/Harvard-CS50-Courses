Convenience store
Video Demo: https://youtu.be/18tfEeWFzis
Definition
This project is order a food item from convenience store.

Project structure :

project.py
test_project.py
requirements.txt
README.md
Libraries
csv : We use csv to read a csv(comma separated value) files.
sys: To exit the program with error message.


Installing Libraries
there is a a requirements.txt file that has all the libraries used.

and simply can be install by this pip command:

pip install -r requirements.txt

Usage
python project.py
Food Item: snacks
Order Item: choco bites
Quantity: 3
Total quantity of  choco bites = 50
Remaining quantity = 47
Total price = $3.0

python project.py
Food Item: food  
Order Item: noodles
Quantity: 4
Total quantity of  noodles = 50
Remaining quantity = 46
Total price = $40.0

python project.py
Food Item: food
Order Item: chicken potpie
Quantity: 4
Total quantity of chicken potpie = 50
Remaining quantity = 46
Total price = $40.0

Functioning
the project.py contains 5 functions including the main function.

main():
This function serves as the entry point of your program.
It prompts the user to input details about a food item, order item, and quantity.
Then it calls various functions to validate inputs and calculate prices.
If any exception occurs during execution, it exits the program with an error message.


check_food_item(food):
This function checks if the provided food item exists in the inventory.
It reads the inventory data from a CSV file and compares the provided food item with the items listed in the inventory.
Returns True if the food item exists, otherwise False.


check_order_item(order, food):
This function checks if the provided order item corresponds to the provided food item.
It reads the inventory data from a CSV file and compares the provided order item with the items listed in the inventory for the given food.
Returns True if the order item exists for the provided food, otherwise it doesn't return anything.


check_quantity(order_item, quantity):
This function checks if the provided quantity is available for the given order item.
It reads the inventory data from a CSV file and checks if the quantity of the specified order item is sufficient.
If the quantity is sufficient, it calculates and prints the remaining quantity.
Returns True if the quantity is sufficient, otherwise it doesn't return anything.


check_price(order_item, quantity):
This function calculates the total price for the given order item and quantity.
It reads the inventory data from a CSV file and retrieves the price of the specified order item.
Then it calculates the total price by multiplying the price with the quantity.
Returns a formatted string representing the total price.


Author : NAVEENKUMAR S.