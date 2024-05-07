# get email from user
email = input("what's your email? ").strip()
# split email in username and domain name
username, domain = email.split("@")
# check username have string and domain have '.' dot
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")