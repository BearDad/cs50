from plates import is_valid


def test_cs50():
    assert is_valid("CS50") == True


def test_cs502():
    assert is_valid("CS05") == False


def test_cs503():
    assert is_valid("PI3.13") == False


def test_cs504():
    assert is_valid("50") == False


def test_cs505():
    assert is_valid("H") == False


def test_cs506():
    assert is_valid("ECTO88") == True

def test_cs507():
    assert is_valid("NRVOUS") == True
def test_cs508():
    assert is_valid("CS50P2") == False
