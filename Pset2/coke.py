def main():
       calculate()


def calculate():
    price = 50
    pay = 0
    while pay < 50:
        c = int(input("Please insert a coin , one at a time? "))
        if c == 5 or c == 10 or c == 25:
            pay += c
            amount_left = price - pay
            if pay > price:
                change = price - pay
                print(f"You Have your coke and a change of {str(change)[1:]} cent")
                break
            elif pay == price:
                print(f"Changed Owed: {amount_left}")
            else:
                print(f"Amount due: {amount_left} cent")
        else:
            print(f"Amount due: {price}")

main()

 
