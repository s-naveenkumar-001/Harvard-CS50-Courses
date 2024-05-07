# we use pytest to test the square function in the calculator file.
# from calculator file we import square function to test that function whether its working as expected or not.

from calculator import square
import pytest
# check positive numbers.
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

# check negative numbers.
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

# check if we give string it shows error as TypeError.
def test_str():
    with pytest.raises(TypeError):
        square("cat")