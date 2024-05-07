def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # vanity plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters(alphabet). so we check zero or first index is alphabet or numberic.
    # if is.alpha is True it go to the next else it return as False. 
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.
    # we check first three is alphabet and fourth one is numeric its break the loop.
    # When isalpha() is True. we add plus one to variable "i". 
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
# After checking alpabet we check the numeric values. if its not numeric its return as false.
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    # No periods, spaces, or punctuation marks are allowed.
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False

    # If we pass all the tests, return True
    return True


if __name__ == "__main__":
    main()