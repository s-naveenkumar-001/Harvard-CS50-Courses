# In this program we import the sys (system) library. we use this library to the command line arguments.
# we use if conition to check the given argument is less than two. if the enter argument is less than two using "sys.exit" it print as "too few arguments" and exit.
# we use for loop to print the given arguments in the separate line.
# In for loop we use " [1:] " means it print the index one from last index. " [1:-1] "" the negative index start from the back side of the command line argument ".
# we also print some particular range using "[1:3]" it will print index one and two.
# using these method we print all command line arguments or particular range command line arguments. 

import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[1:]:
    print("Hello my name is", arg)