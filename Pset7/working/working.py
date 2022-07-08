import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(r"^(?:([0-9]|1[0-2]*)(?::?)*([0-5][0-9])*)? ([A-P]M) to (?:([0-9]|1[0-2]*)(?::?)*([0-5][0-9])*)? ([A-P]M)$", s)
        time_part = matches.groups()
        time1 = new_format(time_part[0],time_part[1],time_part[2])
        time2 = new_format(time_part[3],time_part[4],time_part[5])
    except:
        raise ValueError
    return f"{time1} to {time2}"
        

def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        hour = int(hour)
        if hour ==  12:
            hour = 0
        else:
            hour += 12
    
    if minute == None:
        minute = "00"
        time = f"{str(hour)}:{minute}"
    else:
        time = f"{str(hour)}:{minute}"
 
    return time

if __name__ == "__main__":
    main()

# print(new_format(11, 34, "PM"))