# “hello”, output $0, If the greeting starts with an “h” output $20
# Otherwise, output $100
greeting = input("Greeting: ")
answer =greeting.lower().strip()
if "hello" in answer:
    print("$0")
elif "h" == answer[0]:
    print("$20")
else:
    print("$100")
