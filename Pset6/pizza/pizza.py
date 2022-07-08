import sys
import csv
from tabulate import tabulate


# table = [["Sun", 696000,1989100000],
#         ["Earth", 696000,1989100000],
#         ["Moon", 696000,1989100000],
#         ["Mars", 696000,1989100000]]

# # print(tabulate(table))
# print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29)"]))

menu = []


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()
    

if len(sys.argv) == 2:
    path_extn = sys.argv[1].split(".")
    path_extn = path_extn[-1]
    
    path = sys.argv[1]
    try:
        with open(path) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

    if path_extn != "csv":
        print("Not a CSV file")
        sys.exit()


print(tabulate(menu, headers="firstrow", tablefmt="grid"))