from twttr import shorten


def test_default():
    assert shorten("Twitter") == "Twttr"


def test_sentence():
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_no_vocals():
    assert shorten("CS50") == "CS50"


def test_capitalized():
    assert shorten("PYTHON") == "PYTHN"
