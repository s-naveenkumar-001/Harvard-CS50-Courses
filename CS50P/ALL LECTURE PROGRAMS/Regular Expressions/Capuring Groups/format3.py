import re

name = input("whats your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last, first = matches.group()
    name = first + " " + last
print(f"Hello, {name}")