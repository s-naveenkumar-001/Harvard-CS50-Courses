# In this program we import the sys (system) library. we import this library to use the command line arguments.
# first we import the library and we use error handling method to catch the index error.
# we use try to say hello. if index error happens the except function catch the index error and print as "too few arguments".
# To print the users full name we use double quotation mark in the command line argument to print the full name, ex: "Naveen kumar".
# if we use quotation mark it will consider as single arugument.the python would take the zero index, so we print the index one

import sys

try:
    print("Hello,", sys.argv[1])

except IndexError:
    print("too few arguments")