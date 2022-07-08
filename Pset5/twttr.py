def main():
    user_input = input("Input: ")
    short = shorten(user_input)
    print(short)



def shorten(word):
    vowels = "AEIOUaieou"
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()