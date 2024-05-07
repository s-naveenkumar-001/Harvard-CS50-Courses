# we use command line argument in cowsay program. we enter the string in the command line it will show the trex with hello message.
# import cowsay
# print(cowsay.trex("hello"))

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello," + sys.argv[1])