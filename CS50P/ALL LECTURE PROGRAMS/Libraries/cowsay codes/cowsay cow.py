# we use command line argument in cowsay program. we enter the string in the command line it will show the cow with hello message.
# import cowsay
# print(cowsay.cow("Hello"))

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])