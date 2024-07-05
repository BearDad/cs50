from jar import Jar
from pytest import raises


def test_init():
    Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(11)
    with raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(5)
    assert jar.size == 6
    with raises(ValueError):
        jar.withdraw(8)
