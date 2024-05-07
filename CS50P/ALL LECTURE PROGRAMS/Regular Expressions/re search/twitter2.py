import re 

url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
    if matches.group(1) == "com": 
        print(f"USERNAME:", matches.group(2))