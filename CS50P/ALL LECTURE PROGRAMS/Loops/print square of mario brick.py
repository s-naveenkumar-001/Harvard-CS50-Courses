# print te square of te mario brick using your own functions.
# we use two for loop one is print row another one print the coloumn

def main():
    print_square(3)
# using end="" we print every hashh into single line. using print() we print each row and column three bricks.
def print_square(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()
main()