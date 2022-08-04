from seasons import calc_age
import pytest

def test_valid_format():
    assert calc_age('2021-05-15') == "Six hundred thirteen thousand, four hundred forty minutes"
    assert calc_age('2020-05-15') == "One million, one hundred thirty-nine thousand forty minutes"

def test_invalid_format():
    with pytest.raise(ValueError):
        calc_age('15-07-2022')
        calc_age('January 1, 1999')