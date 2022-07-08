def main():
    question = input("What time is it? ")
    convert(question)


def convert(time):
    hours, minutes = time.split(":")
    hrs = int(hours)
    mins = int(minutes) / 60
    real_time = hrs + round(mins, 2)

    if  real_time <= 8 and real_time >= 7 :
        print("breakfast time")
    elif real_time <= 13 and real_time >= 12:
        print("lunch time")
    elif real_time <= 19 and real_time >= 18:
        print("dinner time")

if __name__ == "__main__":
    main()