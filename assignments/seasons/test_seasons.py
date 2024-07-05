from seasons import t_delta, get_birth
import pytest


def test_t_delta():
    assert (
        t_delta(get_birth("2022-11-01"))
        == "One million, fifty-two thousand, six hundred forty minutes"
    )
    assert (
        t_delta(get_birth("2002-1-3"))
        == "Twelve million, six thousand, seven hundred twenty minutes"
    )
    assert (
        t_delta(get_birth("2100-1-3"))
        == "Minus thirty-nine million, five hundred thirty-six thousand, six hundred forty minutes"
    )
