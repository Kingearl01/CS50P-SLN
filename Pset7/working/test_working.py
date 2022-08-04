from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
        convert("9PM to 9AM")

def test_format1():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_format2():
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"

def test_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 AM")

def test_invalid():
    with pytest.raises(ValueError):
        convert("1 AM 34 AM")
