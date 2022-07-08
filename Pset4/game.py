import random

while True:
    try:
        l = int(input("Level: "))
    except ValueError:
        pass
    else:
        if l > 0:
            break

r = random.randint(1, l)

def guess():
    while True:
        try:
            g = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if g > 0:
                return g



while True:
    g = guess()
    if r == g:
        print("Just right!")
        break        
    elif r < g:
        print("Too large!")
    else:
        print("Too small!")