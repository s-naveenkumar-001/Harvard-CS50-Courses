class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Value")
        self.name = name

...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

...

class Proffessor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

...

wizard = Wizard("Harry")
student = Student("Harry", "Griffindor")
proffessor = Proffessor("Severus", "Defense Against the Dark Arts")
