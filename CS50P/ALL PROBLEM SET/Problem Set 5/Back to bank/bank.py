
def main():
    message = input("Greeting: ")
    Greet = value(message)
    print(Greet)

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting == "hello":
        return "$0"
    elif "h" == greeting[0]:
        return "$20"
    else:
        return "$100"
    
if __name__ == "__main__":
    main()