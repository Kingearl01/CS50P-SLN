months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def validate_date():
    if day < 31 and month < 12:
        return True
    else:
        return False

while True:
    date = input("Date: ")
    f = date.find("/")
    if f == -1:
        
        try:
            if date.find(",") != -1:
                date = date.replace(",", "").title().split()
            mnth = date[0]
            day = int(date[1])
            year = int(date[2])
            month = months.index(mnth) + 1
        except IndexError:
            pass
        except ValueError:
            pass
    else:
        date = date.split("/")
        try:
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])
        except ValueError:
            pass
    try:
        if validate_date() == True:
            break
    except:
        pass

print(f"{year:02}-{month:02}-{day:02}")