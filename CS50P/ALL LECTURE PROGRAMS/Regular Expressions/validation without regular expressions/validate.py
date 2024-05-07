# get email from user
email = input("what's your email? ").strip()
# check '@' in email
if "@" in email:
    print("Valid")
else:
    print("Invalid")