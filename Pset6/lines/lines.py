import sys

count = 0
try:
    path = sys.argv[1]
except IndexError:
    print("Define file path")
    sys.exit()


if len(sys.argv) == 2:
    path_extsn = path.split(".")
    path_extsn = path_extsn[-1]
    if path_extsn != "py":
        print("Not a Python file")
        sys.exit()
 
    try:
        with open(path) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

    for line in lines:
        if line.isspace() == False and line.startswith("#") == False: 
            count += 1
    print(count)
else:
    print("Too many comman-line arguments")


