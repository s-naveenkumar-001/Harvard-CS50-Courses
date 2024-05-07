# we import the requests library to access the web data. using requests.get we access the apple itunes Api json data.
# we use sys command line argument to search the author we want. we use condition in sys to exit the program if any error occurs.
# we import the json library to make the json data readable. we use indent to make at least two spaces in te data.

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(json.dumps(response.json(), indent=2))
