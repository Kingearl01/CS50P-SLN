def main():
    plate = input("Plate: ")
    if middle(plate) and is_valid(plate) and punctuation(plate) and not_number(plate) and first_num(plate):
        print("Valid")
    else:
        print("Invalid")    

def is_valid(s):
    if len(s) > 1 and len(s) < 7:
        return True
    else:
        return False

# check for punctuational marks and spaces
def punctuation(s):
    if s.isalnum() == True:
        return True
    else:
        return False

# check if first two character is not number
def not_number(s):
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    else:
        return True

# first number not zero
def first_num(s):
    i = 0
    if s.isalpha() != True:
        while i < len(s):
            if s[i].isalpha() == False:
                if s[i] == "0":
                    return False 
                else:
                    return True
            i += 1
    else:
        return True

# nuumber is not at the middle
def middle(s):
    # first digit in user inputs
    n = 0
    # first aplha
    a = 0

    # check for alphanumber and find the index of first digit
    for i in range(len(s)):
        if s.isalpha() == True :
            return True

        if s.isalnum() == True:
            if s[i].isdigit() == True:
                n = i
                break
            
    # find the index of the last alpha
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if i > n:
                a = i
                break

    # compare the index of alpha and num
    if n > a :
        return True
    else:
        return False

if __name__ == "__main__":
    main()
