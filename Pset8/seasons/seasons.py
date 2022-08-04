import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    print(calc_age(input("date of Birth: ")))

def calc_age(b):
    today = date.today()
    try:
        birthdate = date.fromisoformat(b)
    except ValueError:
        raise ValueError(f"Invalid Date Format({b}): (YYYY-MM-DD)")

    days = abs(today - birthdate).days

    age_in_minute = p.number_to_words(days * (24 * 60))
    age_in_words = age_in_minute.replace(' and ', " ").capitalize()
    
    return f"{age_in_words} minutes"




if __name__ == "__main__":
    main()

# print(date.fromisoformat('2021-05-15'))
