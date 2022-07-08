def main():
    var = input("Give a name to your variable? ")
    camelCase(var)


def camelCase(s):
    for c in s:
        if c >= "A" and c <= "Z":
            s = s.replace(c, f"_{c.lower()}")
    print(s)


main()

