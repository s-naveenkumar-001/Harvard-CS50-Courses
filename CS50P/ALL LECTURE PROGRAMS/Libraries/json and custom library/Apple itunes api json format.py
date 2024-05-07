# we import the requests library to access the web data. using requests we access the apple itunes Api json data.
# we use sys command line argument to search the author we want. we use condition in sys to exit the program if any error occurs.
# create a variable called response to store the json data and using reponse.json() print the json data.

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())