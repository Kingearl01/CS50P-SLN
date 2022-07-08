items = {}

while True:
    print(items)
    try:
        item = input("Item: ").strip().upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        for key in sorted(items.keys()):
            # print(items[key], key)
            # print()
            break

# items = {"ORANGE": 2,
#     "KIWI": 2,
#     "MANGO": 1}
for i in items:

    print(items[i], i)