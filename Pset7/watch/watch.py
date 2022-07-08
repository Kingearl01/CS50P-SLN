import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r'(https?://(?:www.)youtube.com/)embed/(\w+)', s)
    try:
        url = matches.group(1) + matches.group(2)
    except AttributeError:
        return None

    
    return re.sub(matches.group(1), "https://youtu.be/", url)
        
        


if __name__ == "__main__":
    main()
