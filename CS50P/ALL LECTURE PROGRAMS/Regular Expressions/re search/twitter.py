
import re 

url = input("URL: ").strip()
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"USERNAME: {matches.group(2)}")