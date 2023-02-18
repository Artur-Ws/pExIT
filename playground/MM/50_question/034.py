import pytest
import unittest


def dodawanie(a, b):
    return a + b + 1


def test_dodawania_intow():
    assert dodawanie(2, 3) == 5


def test_dodawanie_stringow():
    assert dodawanie('a', 'b') == 'ab'



