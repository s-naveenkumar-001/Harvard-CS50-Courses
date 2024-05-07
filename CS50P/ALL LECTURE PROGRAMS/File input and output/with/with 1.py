# We use 'with' keyword to open and close the file automatically.
# In 'open' keyword Using 'a' we can read and write the file.
name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")