import inflect
p = inflect.engine()

lyrics = "Adieu, adieu to"
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break


print("Adieu, adieu to " + p.join(name))
