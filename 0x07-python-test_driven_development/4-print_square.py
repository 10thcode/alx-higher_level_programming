#!/usr/bin/python3
"""
This module define a function that prints a square with the character #.
>>> print_square(1)
#
"""


def print_square(size=1):
    """
    A function that prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
