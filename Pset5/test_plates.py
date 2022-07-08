from plates import punctuation, not_number, is_valid, first_num, middle

def test_middle():
    assert middle("CS501") == True
    assert middle("CS50P") == False

def test_first_digit():
    assert first_num("CS50") == True
    assert first_num("CS05") == False
    assert first_num("C0S5XP") == False



def test_first_two_char():
    assert not_number("CS50") == True
    assert not_number("CS50P") == True
    assert not_number("11CS50") == False
    assert not_number("C0S50") == False
    assert not_number("2CS50") == False


def test_punctuation():
    assert punctuation("CS50.P")  == False
    assert punctuation("C@S50") == False
    assert punctuation("CS501") == True


def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("CSP5050") == False
    assert is_valid("CCCCCCCCCC") == False
    assert is_valid("111111") == True