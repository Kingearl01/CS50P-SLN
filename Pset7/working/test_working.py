from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
        convert("9 PM - 9 AM")

def test_time():
    assert convert("9 PM to 9 AM") == "21:00 to 9:00"
    assert convert("10:30 PM to 8:30 AM") == "22:30 to 8:30"

def test_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 AM")

def test_hour():
    with pytest.raises(ValueError):
        convert("16 AM to 13 AM")
        convert("09:00 AM to 17:00 PM")
         