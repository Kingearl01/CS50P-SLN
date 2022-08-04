from validator_collection import validators, checkers, errors
def main():
    print(validate(input("What's your email address? ")))
# email_address = validators.email('this-is-an-invalid-email')

# print(email_address)


def validate(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"
# print(checkers.is_ip_address('127.1.1.0'))

if __name__ == "__main__":
    main()