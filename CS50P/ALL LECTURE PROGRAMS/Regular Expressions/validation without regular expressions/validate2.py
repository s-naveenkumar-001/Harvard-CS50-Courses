# get email from user
email = input("what's your email? ").strip()
# check @ and dot '.' in email.
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")