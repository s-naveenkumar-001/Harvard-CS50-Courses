import re

email = input("what's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")