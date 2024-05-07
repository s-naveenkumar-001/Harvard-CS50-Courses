# In this program we import the sys (system) library. we import this library to use the command line arguments.
# In this program we use conditions.if user enter less than two argument it print as "too few arguments".
# elif user enter greater than two argument it print as too many argumants.
# else it will print as "Hello my name is" and user enter argument.

import sys

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("Hello, my name is", sys.argv[1])