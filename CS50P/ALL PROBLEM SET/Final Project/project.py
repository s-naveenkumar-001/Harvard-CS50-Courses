import csv
import sys


def main():
    try:
        food = input("Food Item: ").lower()
        order_item = input("Order Item: ").lower()
        quantity = int(input("Quantity: "))
        if check_food_item(food) == True:
            pass
        if check_order_item(order_item, food) == True:
            if check_quantity(order_item, quantity) == True:
                print(check_price(order_item, quantity))
        else:
            print("Invalid input")
    except:
        sys.exit("Provide a valid input for food, order_item and quantity")


def check_food_item(food):
    store_item = []
    with open("Inventory.csv") as csvfile:
        file = csv.DictReader(csvfile)
        for line in file:
            store_item.append(line["Food"].lower())
    if food in store_item:
        return True
    else:
        return False


def check_order_item(order, food):
    store_item = []

    with open("Inventory.csv") as csvfile:
        file = csv.DictReader(csvfile)
        for line in file:
            store_item.append({line["ItemName"].lower(): line["Food"].lower()})
        for list in store_item:
            if order in list:
                add = list[order]
                if food in add:
                    return True
                else:
                    return False


def check_quantity(order_item, quantity):
    quantity_data = []

    with open("Inventory.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            quantity_data.append({row["ItemName"].lower(): row["Quantity"]})

        for list in quantity_data:
            if order_item in list:
                if quantity > int(list[order_item]):
                    print(f"We have only have {list[order_item]} quantity in {order_item}")
                    return False
                remain_quantity = int(list[order_item]) - quantity
                print(f"Total quantity of {order_item} = {int(list[order_item])}")
                print(f"Remaining quantity = {remain_quantity}")
                return True


def check_price(order_item, quantity):
    item_price = []
    with open("Inventory.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item_price.append({row["ItemName"].lower(): row["Price"]})

        for item in item_price:
            if order_item in item:
                price = item[order_item]
                price = price.replace("$", "")
                total_price = quantity * float(price)
                return f"Total price = ${float(total_price)}"


if __name__ == "__main__":
    main()