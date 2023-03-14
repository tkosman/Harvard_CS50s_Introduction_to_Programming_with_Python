from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("2/3") == 67
    assert convert("1/4") == 25

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("10/0")
    with pytest.raises(ValueError):
        convert("1/%")
        convert("#/10")
        convert("4/1")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(90) == "90%"