import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r'https?://(?:www\.)?youtube\.com/embed/(\w+)"', s)
    
    try:
        return f"https://youtu.be/{matches.group(1)}"
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
