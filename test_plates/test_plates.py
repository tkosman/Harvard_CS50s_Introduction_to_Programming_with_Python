from plates import is_valid

def test_one():
    assert is_valid("A23") == False
    assert is_valid("A23BB") == False

def test_two():
    assert is_valid("AA0000003") == False
    assert is_valid("A") == False

def test_three():
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False

def test_four():
    assert is_valid("A L") == False
    assert is_valid("A.L") == False
    assert is_valid("A-L") == False
    assert is_valid("&&&") == False

def test_five():
    assert is_valid("&&&") == False