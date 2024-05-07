#Get input from user and replace the whitespace into (...)
message = input("what would you like to say: ").strip()
message1 = message.replace(" ", "...")
print(message1)