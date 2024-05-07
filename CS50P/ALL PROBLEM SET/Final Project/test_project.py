from project import check_food_item, check_order_item, check_quantity, check_price

def main():
    test_check_food_item()
    test_check_order_item()
    test_check_quantity()
    test_check_price()


def test_check_food_item():
    assert check_food_item("drinks") == True
    assert check_food_item("food") == True
    assert check_food_item("snacks") == True
    assert check_food_item("abcd") == False
    assert check_food_item("sushi") == False

def test_check_order_item():
    
    assert check_order_item("fiji", "drinks") == True
    assert check_order_item("noodles", "food") == True
    assert check_order_item("choco bites", "snacks") == True
    assert check_order_item("aquafina", "snacks") == False
    assert check_order_item("noodles", "drinks") == False

def test_check_quantity():
    assert check_quantity("fiji", 8) == True
    assert check_quantity("choco bites", 10) == True
    assert check_quantity("noodles",12) == True
    assert check_quantity("bbq chips", 15) == False
    assert check_quantity("milk chocolate bar", 16) == False


def test_check_price():
    assert check_price("choco bites", 4) == "Total price = $4.0"
    assert check_price("noodles", 2) == "Total price = $20.0"
    assert check_price("fiji", 8) == "Total price = $16.0"