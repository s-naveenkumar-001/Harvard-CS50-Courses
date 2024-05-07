import csv
# get value from user.
name = input("What's your name? ")
home = input("Where's your home? ")

# write dictionary values to the csv file.
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
    