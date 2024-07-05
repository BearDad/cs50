from fuel import convert, gauge
import pytest


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == f"{50}%"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_Value_Error():
    with pytest.raises(ValueError):
        convert("cat/cat")


def test_convert():
    assert convert("1/2") == 50
