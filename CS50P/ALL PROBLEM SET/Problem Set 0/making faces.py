# Get unput from user and create a function called convert and print
def main():
    message = input("what would you like to say: ")
    result = convert(message)
    print(result)
# using replace ":)" into "🙂" nad ":(" into "🙁" and return the value 
def convert(nam):
    nam1 = nam.replace(":)", "🙂")
    nam2 = nam1.replace(":(", "🙁")
    return nam2
main()
