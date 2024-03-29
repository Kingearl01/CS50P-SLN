import re

def main():
    print(validate(input("IP4V Address: ").strip()))
# digit = "^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"

def validate(ip):
# if re.search("^[\d]+\.[\d]+\.[\d]+\.[\d]+", ip):
    if re.search(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()