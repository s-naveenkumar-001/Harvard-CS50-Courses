
import sys
import csv
from tabulate import tabulate

def main():
    check_command_line()
    # Create variable to store the table data
    table = []
    # Try to open the file
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
    # If can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exit")
    print(tabulate(table[1:], table[0], tablefmt="grid"))

def check_command_line():
     #Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line argumnets")
        # Check if it is a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file")

if __name__ == "__main__":
    main()
