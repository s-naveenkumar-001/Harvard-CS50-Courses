# print students name and their houses in the csv file.
# split() function split the values into two pieces.
with open("students.csv") as file:
    for line in file:
        # we store the splited values into separate variables.
        name, house = line.rstrip().split(",")  
        print(f"{name} is in {house}")
