# In while loop we use erroe handling method until user enters integer it continue the loop.

while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"{x} is an integer")