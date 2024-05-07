# " Number Guessing Game ".

# import the random library after reading documendation we use randint to guess the number.
# Using while loop we prompt the user and we try and except, in try we get input from user. 
# If user enter integer greater than zero using break we get out of the loop.
# If any error occurs using except we catch the error and using "pass" we say nothing.
import random

while True:
    try:
        level =int(input("Level: "))
        if level > 0:
            break

    except:
        pass

# using randint we generate the random number in between one to user entered number.
Random_Number = random.randint(1, level)
# Using while loop we prompt the user and we use try and except. In guess we get input from user and if user entered number is greater than zero.
# if guess less than Random_Number print("Too small!").Repromt the user and he guess the correct number.
# elif guess greater than Random_Number print("Too large!").
# else print("Just right!") and using break get out of the loop.
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0 :
            if guess < Random_Number:
                print("Too small!")
            elif guess > Random_Number:
                print("Too large!")
            else:
                print("Just right!")
                break
# we catch the error and using pass we say nothing.
    except:
        pass

        
