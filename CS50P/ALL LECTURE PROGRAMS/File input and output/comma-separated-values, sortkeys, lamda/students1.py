# print students name and their houses in the csv file.
# split() function split values into two pieces and it plit vlalues into list.
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        # the splited values stored in row as a list. we print zero and first index of the list.  
        print(f"{row[0]} is in {row[1]}")
