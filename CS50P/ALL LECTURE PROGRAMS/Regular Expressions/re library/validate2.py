# import re library
import re
# get email from user
email = input("what's your email? ").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")