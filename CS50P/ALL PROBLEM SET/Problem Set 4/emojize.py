# we install the emoji library in our system. using import function we import the emoji library in our program.
# we get the text input from user and we store that value in user_ answer variable.
# After reading emoji library documentation. using emoji library and format string we print the text input into emoji output.

import emoji

user_answer = input("Input: ")
print(emoji.emojize(f"Output: {user_answer}", language="alias"))
