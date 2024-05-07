# The default program we need to implement a vanity plate in is_valid function
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# we need assign a letter between 2 to 6 and number come at the last only like "AAA222" not like "AA22AA"
# if and else condition if its true it will return true or else false
def is_valid(b):
    if 6 >= len(b) >= 2 and b [0:2].isalpha() and b.isalnum():
        for char in b:
            if char.isdigit():
                index = b.index(char)
                if b[index:].isdigit()and int(char) !=0:

                        return True
                else:
                    return False
        return True

main()