# This code for understand the ' str ' method to print the string values
# Read the notion notes to understand to understand the concept
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ") 
    house = input("House: ") 
    return Student(name, house)


if __name__ == "__main__":
    main()