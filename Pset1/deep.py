def main():
    answer(question)
question = input("What is the Answer to the Great Question of Life, the Universe, and Everyting? ").lower().strip()


# def answer(to):
#     if to == "42":
#         print("Yes")
#     elif to == "forty-two":
#         print("Yes")
#     elif to == "forty two":
#         print("Yes")
#     else:
#         print("No")

def answer(to):
    if to == "42" or to == "forty-two" or to == "forty two":
        print("Yes")
    else:
        print("No")

main()