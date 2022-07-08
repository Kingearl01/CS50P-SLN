from fuel import convert, gauge

def test_convert():
    assert convert("2/3") == 67
    assert convert("1/15") == 7
    assert convert("-2/3") == -67

def test_gauge():
    assert gauge(45) == "45%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(-12) == "E"
    assert gauge(2.4) == "2.4%"
