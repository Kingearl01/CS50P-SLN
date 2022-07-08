import csv
import sys

casts = []

if len(sys.argv) < 3:
    print("To few command-line arguments")
    sys.exit()
elif len(sys.argv) > 3:
    print("To many command-line arguments")
    sys.exit()

if len(sys.argv) == 3:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                casts.append({"name": row['name'], "house": row['house']})
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")

    for i in casts:
        first, last = (i['name']).split(",")
        house = i['house']
        with open(sys.argv[2], "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerow({'first': first, 'last': last, 'house': house})