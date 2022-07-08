def main():
    file = input("File name: ").lower().strip()
    get_extension(file)

#  1st method
# def get_extension(n):
#     if n.find(".gif") !=  -1:
#         print(n.replace(n, "image/gif"))
#     elif n.find(".jpg") != -1 or n.find(".jpeg") != -1:
#         print(n.replace(n, "image/jpeg"))
#     elif n.find(".png") != -1:
#         print(n.replace(n, "image/png"))
#     elif n.find(".txt") != -1:
#         print(n.replace(n, "text/plain"))
#     elif n.find(".zip") != -1:
#         new_n = n.replace(n, "application/zip")
#         print(new_n)
#     elif n.find(".pdf") != -1:
#         new_n = n.replace(n, "application/pdf")
#         print(new_n)
#     else:
#         print("application/octet-stream")


# main()

# Modified
def get_extension(t):
    # seperate with .
    s = t.split(".")
    # length of s
    l = len(s)
    # last index
    last_index = s[l - 1]

    if  last_index == "pdf" or last_index == "zip":
        new_n = t.replace(t , f"application/{last_index}")
        print(new_n)
    elif  last_index == "txt":
        new_n = t.replace(t, "text/plain")
        print(new_n)
    elif last_index == "jpeg" or last_index == "gif" or last_index == "png" or last_index == "png":
        new_n = t.replace(t, f"image/{last_index}")
        print(new_n)
    elif last_index == "jpg":
        new_n = t.replace(t, "image/jpeg")
        print(new_n)
    else:
        print("application/octet-stream")

main()