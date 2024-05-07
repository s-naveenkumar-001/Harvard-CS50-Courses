# import re library
import re 
email = input("what's your email? ").strip()
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
    