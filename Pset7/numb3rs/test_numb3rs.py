from numb3rs import validate

def test_valid_ip():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True



def test_alphabet():
    assert validate("cat") == False

def test_invalid_ip():
    assert validate("64.128.256.512") == False
    assert validate('2550:255.255:255') == True
