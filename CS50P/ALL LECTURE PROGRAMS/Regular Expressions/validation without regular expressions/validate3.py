# get email from user
email = input("what's your email? ").strip()
# check '@' and email endswith(".edu").
if "@" in email and email.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")