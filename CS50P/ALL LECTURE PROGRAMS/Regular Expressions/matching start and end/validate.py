import re
# get email from user
email = input("what's your email? ")
if re.search(r"^.+@.+\.edu$", email) :
    print("Valid")
else:
    print("Invalid")