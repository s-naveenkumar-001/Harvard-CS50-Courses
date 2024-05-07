# we import the square function and we test the function output using conditions.
from calculator import square

def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 square is not 4")
    if square(3) != 9:
        print("3 square is not 9")


if __name__ == "__main__":
    main()