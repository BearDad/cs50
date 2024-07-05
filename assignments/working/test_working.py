from working import convert
import pytest


def test_AM_PM_NO_DOTS():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_AM_PM():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_AM_PM_MIXED():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_PM_AM_MIXED():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_ValueError_Range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 17:60 PM")


def test_Wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM   10 PM")


def test_ValueError():
    with pytest.raises(ValueError):
        convert("9:60 AM to 17:60 PM")
