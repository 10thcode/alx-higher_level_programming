#!/usr/bin/python3
"""
This module contains a function to add to integers
>>> add_integer(2, 2)
4
"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.
    """
    if a != a or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if b != b or type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    if result == float("inf") or result == -float("inf"):
        raise ValueError("float overflow")
    return result
