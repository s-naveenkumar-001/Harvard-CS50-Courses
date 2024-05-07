# constant variable in class with uppercase
class Cat:
    MEOW = 3

    def meow(self):
        for _ in range(Cat.MEOW):
            print("meow")

cat = Cat()
cat.meow()