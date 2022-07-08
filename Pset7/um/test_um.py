from um import count


def test_default():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um......") == 2


def test_part_of_word():
    assert count("yummy") == 0

def test_begining():
    assert count("umbralla") == 1