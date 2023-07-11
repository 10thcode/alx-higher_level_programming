#!/usr/bin/python3
"""
This module defines a a function that adds
a new attribute to an object if it’s possible
"""


def add_attribute(obj, key, value):
    """ adds a new attribute to an object if it’s possible """
    if type(obj).__name__ not in dir(__import__("builtins")):
        if "__slots__" not in dir(obj) or key in obj.__slots__:
            setattr(obj, key, value)
            return None
    raise TypeError("can't add new attribute")
