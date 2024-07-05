from bank import value


def test_1():
    assert value("hello") == 0
    print(value)

def test_2():
    assert value(" How you doing?") == 20
    print(value)

def test_3():
    assert value("Whatever") == 100
    print(value)