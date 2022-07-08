def main():
    convert()

def convert():
    word = input("Please type any text ").replace(":)", "🙂")
    print(word.replace(":(", "🙁"))

main()