# import random , sys and figlet libraries.
# Using figlet library make user input text into FIGLET font.
# Among the fonts supported by FIGlet are those at " figlet.org/examples.html ".

import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font" ):
    isRandomFont = False
else:
    sys.exit(1)


figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)

else:
    font = random.choice(figlet.getFonts())

msg = input("Input: ")

print("Output: ")
print(figlet.renderText(msg))