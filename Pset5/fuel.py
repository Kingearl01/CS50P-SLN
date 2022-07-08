def main():
    fuel = input("Fraction: ")
    print(gauge(convert(fuel)))

def convert(fraction):
    try:
        fraction = fraction.split("/")
        x = int(fraction[0])
        y = int(fraction[1]) 
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if x > y:
            raise ValueError() 
    except:
        raise ValueError("x or y not integer or x is greater than y")
    fuel_percent = (x/y) * 100
    return round(fuel_percent)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    

    
if __name__ == "__main__":
    main()