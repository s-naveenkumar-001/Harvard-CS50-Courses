import csv

def main():
    food = input("Food Item: ").lower()
    order_item = input("Order Item: ").lower()
    if check_food_item(order_item) == food:
        print("drinks")
    else:
        print("False")
    #check_food_item(food)


def check_food_item(food):
    store_item = []
    with open("Inventory.csv") as csvfile:
        file = csv.DictReader(csvfile)
        for line in file:
            store_item.append({line["ItemName"].lower() : line["Food"].lower()})
        for store in store_item:
            if food in store:
                 return store[food]
            else:
                return False
                
        

 
if __name__ == "__main__":
    main()
