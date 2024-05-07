# import re library
import re
# get email from user
email = input("what's your email? ").strip()
# check '@' in email
if re.search("@", email):
    print("Valid")
else:
    print("Invalid")