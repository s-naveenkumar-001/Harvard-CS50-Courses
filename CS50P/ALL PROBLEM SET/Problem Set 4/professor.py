# After reading random library documendation. we import from random library we import random.randint() to generate the random number.
# In the main function we call get_level() to get the level input from user.Using simulate_game() we get the score points.
# Using print function function we print the score. 

from random import randint

def main():
    level = get_level()
    score = simulate_game(level)
    print("Score: ", score)

# check whether the user input level is in the list or not. if any error occurs catch the error and say nothing.
# return the input value.
def get_level():
    while True: 
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

# print difficulty based on level and generate random number x and y. and return the value.
def generate_integer(level):
    if level == 1:
        x = randint(0,9)
        y = randint(0,9)
    elif level == 2:
        x = randint(10,99)
        y = randint(10,99)
    else:
        x = randint(100,999)
        y = randint(100,999)
    return x,y
# if user enter wrong answer more than three times.print the correct answer for that sum.
def simulate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
            pass
    print(f"{x} + {y} = {x+y}")
    return False 
# print ten rounds and return score points. 
def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = simulate_round(x, y)
        if response == True:
            score += 1
        count_round += 1
    return score

# we call the main function.
if __name__ == "__main__":
    main()
