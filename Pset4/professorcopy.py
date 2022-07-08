import random
from tkinter import Y

def main():
    level = get_level()
    score = simulate_game(level)
    print("score: ", score)
    # simulate_round(8, 2)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def simulate_round(x,y):
    life = 1
    while life <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
        except:
            life += 1
            print("EEE")
            # print(life)
        else:
            if answer == (x + y):
                return True
            else:
                life += 1
                print("EEE")
                # print(life)    
    print(life)
    print(f"{x} + {y} = {x + y}")
    # return False

def simulate_game(level):
    score = 0
    round = 1

    while round <= 10:
        x,y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score += 1
        round += 1

    return score

if __name__ == "__main__":
    main()