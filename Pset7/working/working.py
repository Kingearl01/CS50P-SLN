import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(r"^([0-9]|1[0-2]*):*([0-5][0-9])* ([A-P]M) to ([0-9]|1[0-2]*):*([0-5][0-9])* ([A-P]M)$", s)
        time_part = matches.groups()

        time1 = new_format(time_part[0],time_part[1],time_part[2])
        time2 = new_format(time_part[3],time_part[4],time_part[5])
    except AttributeError:
        raise ValueError()

    return f"{time1} to {time2}"
        

def new_format(hour, minute, am_pm):
    hour = int(hour)
    if am_pm == "PM":
        if hour ==  12:
            hour = 12
        else:
            hour += 12
    if am_pm == "AM":
        if hour == 12:
            hour = 0

    if minute == None:
        minute = 0

    return f"{hour:02}:{int(minute):02}"
        
 


if __name__ == "__main__":
    main()
# print(convert('9 AM to 10 PM'))
# print(convert('9:45 AM to 10:45 PM'))
# print(new_format(9, None, "PM"))