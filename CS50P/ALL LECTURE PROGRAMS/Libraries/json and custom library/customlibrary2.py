# we import the sys to use the command line argumants and from the customlibrary we import the hello().
# Using condition and len function in sys.if "len(sys.argv)" is equal to two. it execute the hello function.
# in the hello function we print the "sys.argv[1]"" index one.

import sys
from customlibrary import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])