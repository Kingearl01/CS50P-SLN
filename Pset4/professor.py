import sys
import random
from unittest import result

def main():
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        get_level(level) 
        score = 0
        life = 3
        round = 1
        while round <= 10:
            x = generate_integer(level)  
            y = generate_integer(level)
            answer =  x + y
            reponse = int(input(f"{x} + {y} = "))
            if (x + y) == reponse:
                score += 1
            else:
                stimulate_game()
             
            round += 1

def get_level(level):
    while True:
        try:
            # level = int(input("level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass
        # else:
        #     raise ValueError


def generate_integer(level):
    global x, y
    if level == 1:
       return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

def stimulate_game():
    life  =  3
    x = generate_integer(level)  
    y = generate_integer(level)
    while life > 0:
        if 
# def stimulate_round():
#     life = 3
#     x,y = generate_integer(get_level())

#     while life > 0:
#         try:
#             user_answer = int(input(f"{x} + {y} = "))
#         except ValueError:
#             life -= 1
#             print("EEE")
#         else:
#             if user_answer == (x + y):
#                 n_question = 1
#                 score = 0
#                 while n_question <= 10:
#                     n_question += 1
#                     score += 1
#             else:
#                 life -= 1
#                 print("EEE")
#     print(f"Correct answer: {x + y}")
# stimulate_round()
# def stimulate_game():
#     n_question = 1
#     score = 0
#     while n_question <= 10:
#         x, y = generate_integer(get_level())
#         response = stimulate_round(x,y)
#         if response == True:
#             score += 1
        
#         n_question += 1
#         return score

if __name__ == "__main__":
    main()