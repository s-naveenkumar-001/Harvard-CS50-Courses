import re

email = input("what's your email? ").strip()
if re.search("^\w+@\w+\.edu", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")