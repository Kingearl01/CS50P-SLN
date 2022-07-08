import emoji
def main():
    text = input("Input: ").strip()
    print("Output: ", emoji.emojize(text))

def generate(emo):
    return emoji.emojize(emo)

# main()

print(emoji.emojize(":smile_cat:"))