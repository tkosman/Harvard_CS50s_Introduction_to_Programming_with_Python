from twttr import shorten

def test_A():
    assert shorten("GHA") == "GH"
    assert shorten("AGA") == "G"

def test_U():
    assert shorten("JUP") == "JP"
    assert shorten("FUJ") == "FJ"

def test_numbers():
    assert shorten("A0J") == "0J"

def test_omit_punct():
    assert shorten("A.J") == ".J"

def test_small():
    assert shorten("jak") == "jk"