# print the square of the number,
# using unit test test this code whether its give te excepted output or not.

def main():
    x = int(input("What's x? "))
    print(f"{x} squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
