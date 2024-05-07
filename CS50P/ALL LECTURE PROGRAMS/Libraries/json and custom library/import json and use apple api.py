
# we import the requests library to access the web data. using requests we access the apple itunes Api json data.
# we use sys command line argument to search the author we want. we use condition in sys to exit the program if any error occurs.
# create a variable called response to store the json data. we create r to store the response.json() data.
# Using for loop we store the r["results"] in the result and we print the each trackName in the result.
# we print fifty song name in the Apple itunes using author name.

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
r = response.json()
for result in r["results"]:
    print(result["trackName"])