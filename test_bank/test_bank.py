from bank import value

def test_if_works():
    assert value("hello you") == 0
    assert value("hi") == 20
    assert value("innt") == 100

def test_if_works():
    assert value("Hello you") == 0
    assert value("Hi") == 20
    assert value("iNnt") == 100