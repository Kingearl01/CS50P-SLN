from response import validate

def test_email():
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("malan@@@harvard.edu") == "Invalid"