from bank import value

def test_first_letter():
    word_1 = "hey"
    word_2 = "hi"
    word_3 = "happy"
    assert value(word_1[0]) == 20
    assert value(word_2[0]) == 20
    assert value(word_3[0]) == 20


def test_first_word():
    assert value('hello') == 0

def test_other():
    assert value("what's Up") == 100
    assert value("what's Up") == 100