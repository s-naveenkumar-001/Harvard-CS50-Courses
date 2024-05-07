# test the calculator sqaure function.
from calculator import square

# check the positive numbers.
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

# check negative numbers.
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

# check zero equal to zero.
def test_zero():
    assert square(0) == 0