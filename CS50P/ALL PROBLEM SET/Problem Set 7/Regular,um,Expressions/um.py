import re

def main():
    print(count(input("Text: ")))


def count(s):
    um_list = re.findall(r"(^|\W)um($|\W)", s, re.IGNORECASE)
    return len(um_list)

if __name__ == "__main__":
    main()
