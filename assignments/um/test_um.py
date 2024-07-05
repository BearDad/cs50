from um import count
import pytest


def test_count_none():
    assert (
        count(
            "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
        )
        == 2
    )


def test_count():
    assert count("um") == 1


def test_count2():
    assert count("Um") == 1


def test_count3():
    assert count("hello, um, world") == 1
    assert count("hello, um, Um... world") == 2
    assert count("hello, um, Um... yummy") == 2
