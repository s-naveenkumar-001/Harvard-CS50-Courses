# In this program we import the sys (system) library. we import this library to use the command line arguments.
# we use sys.exit in conitions. when the condition satisfy it print the given instruction and exit the program. 
# if both condition are not satify. it will execute the print statement.

import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

print("Hello, my name is", sys.argv[1])