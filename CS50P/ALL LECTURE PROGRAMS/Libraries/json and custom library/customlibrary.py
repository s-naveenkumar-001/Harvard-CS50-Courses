# we create our own library to use this library in our programs.
# we create two function called hello() and goodbye(). in this function we use format string to print "Hello, world".
# we use if __name__ == "__main__" to run this library into another program. using these we run the particular function in the library. it also run this library too.
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Hello, {name}")

if __name__ == "__main__":
    main()