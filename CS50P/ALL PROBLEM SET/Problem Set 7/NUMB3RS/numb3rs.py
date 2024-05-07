import re

# prompt the user for ip address
def main():
    print(validate(input("IPv4 Address: ")))

# check the ip address is valid ipv4 adress or not
def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        split_ip = ip.split(".")
        for piece in split_ip:
            if int(piece) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()