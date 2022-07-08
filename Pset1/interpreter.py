def main():
    expression = input("Expression: ").split()
    # calculate(expression)
    get_Operation(expression)

# def calculate(n):
#     n.split()
#     x = n[0]
#     y = n[1]
#     z = n[2]


def get_Operation(p):

    x = float(p[0])
    y = p[1]
    z = float(p[2])

    if y == "+":
        result = x + z
        print(round(result, 1))
    elif y == "-":
        result = x - z
        print(round(result, 1))
    elif y == "*":
         result = x * z
         print(round(result, 1))
    else:
        if y == "/" and z == 0:
            print("Can't divide by Zero (0)")
        else:
            result = x / z
            print(round(result, 1))
            
        

main()


# f ="1 + 1"
# f.split()
# y = f[1]
# print(y)
# print(f[1] == "+")