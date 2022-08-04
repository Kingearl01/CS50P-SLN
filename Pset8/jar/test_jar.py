from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12



def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposite(1)
    assert str(jar) == "🥧"

    jar.deposite(11)
    assert str(jar) == "🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧"


def test_deposite():
    jar = Jar()
    jar.deposite(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposite(9)
        jar.deposite(11)


def test_withdraw():
    jar = Jar()
    jar.deposite(6)
    jar.withdraw(5)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(10) 