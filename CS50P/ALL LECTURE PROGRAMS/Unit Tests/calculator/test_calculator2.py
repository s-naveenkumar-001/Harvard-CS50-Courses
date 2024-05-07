# from calculator file import square function and test the square function using pytest.
# using assert check the output. if any error occurs catch the error using error handling method.
from calculator import square

def main():
    test_square()

# check square function and catch the errors.
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square is not equal to 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square is not equal to 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square is not equal to 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square is not equal to 9")
        

if __name__ == "__main__":
    main()