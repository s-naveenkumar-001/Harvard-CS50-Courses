import re 

url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z-0-9_]+)", url, re.IGNORECASE):
    print(f"USERNAME: {matches.group(1)}")