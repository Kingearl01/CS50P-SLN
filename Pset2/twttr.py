def main():
    user_input = input("Input: ")
    remove(user_input)



def remove(v):
    vowels = "AEIOUaieou"
    for vowel in vowels:
        v = v.replace(vowel, "")
    print(f"Output: {v}")


main()